#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <MLV/MLV_all.h>

#define WIDTH 800
#define HEIGHT 600
#define GRID_SIZE 20
#define MAX_SNAKE_SIZE 100

typedef struct {
    int x;
    int y;
} Position;

typedef struct {
    Position position;
    int size;
    Position body[MAX_SNAKE_SIZE];
} Snake;

typedef struct {
    Position position;
    MLV_Color color;
} Food;

typedef struct {
    Position position;
    MLV_Color color;
} Obstacle;

typedef enum {
    UP,
    DOWN,
    LEFT,
    RIGHT
} Direction;

void draw_snake(Snake* snake) {
    MLV_draw_filled_rectangle(snake->position.x * GRID_SIZE, snake->position.y * GRID_SIZE, GRID_SIZE, GRID_SIZE, MLV_COLOR_GREEN);

    for (int i = 0; i < snake->size; i++) {
        MLV_draw_filled_rectangle(snake->body[i].x * GRID_SIZE, snake->body[i].y * GRID_SIZE, GRID_SIZE, GRID_SIZE, MLV_COLOR_GREEN);
    }
}

void draw_food(Food* food) {
    MLV_draw_filled_rectangle(food->position.x * GRID_SIZE, food->position.y * GRID_SIZE, GRID_SIZE, GRID_SIZE, food->color);
}

void draw_obstacle(Obstacle* obstacle) {
    MLV_draw_filled_rectangle(obstacle->position.x * GRID_SIZE, obstacle->position.y * GRID_SIZE, GRID_SIZE, GRID_SIZE, obstacle->color);
}

void move_snake(Snake* snake, Direction direction) {
    for (int i = snake->size - 1; i > 0; i--) {
        snake->body[i] = snake->body[i - 1];
    }

    snake->body[0] = snake->position;

    switch (direction) {
        case UP:
            snake->position.y--;
            break;
        case DOWN:
            snake->position.y++;
            break;
        case LEFT:
            snake->position.x--;
            break;
        case RIGHT:
            snake->position.x++;
            break;
    }
}

int check_collision(Snake* snake, Food* food, Obstacle* obstacles, int num_obstacles) {
    if (snake->position.x < 0 || snake->position.x >= (WIDTH / GRID_SIZE) ||
        snake->position.y < 0 || snake->position.y >= (HEIGHT / GRID_SIZE)) {
        return 1; // Collision avec les bords de la fenêtre
    }

    for (int i = 0; i < snake->size; i++) {
        if (snake->body[i].x == snake->position.x && snake->body[i].y == snake->position.y) {
            return 1; // Collision avec le corps du serpent
        }
    }

    for (int i = 0; i < num_obstacles; i++) {
        if (obstacles[i].position.x == snake->position.x && obstacles[i].position.y == snake->position.y) {
            return 1; // Collision avec un obstacle
        }
    }

    if (snake->position.x == food->position.x && snake->position.y == food->position.y) {
        return 2; // Collision avec une pomme
    }

    return 0; // Pas de collision
}

void generate_food(Food* food, Snake* snake, Obstacle* obstacles, int num_obstacles) {
    food->position.x = rand() % (WIDTH / GRID_SIZE);
    food->position.y = rand() % (HEIGHT / GRID_SIZE);

    /* Vérifier que la nourriture n'apparaît pas sur le serpent ou un obstacle */
    while (food->position.x == snake->position.x && food->position.y == snake->position.y) {
        food->position.x = rand() % (WIDTH / GRID_SIZE);
        food->position.y = rand() % (HEIGHT / GRID_SIZE);
    }

    for (int i = 0; i < num_obstacles; i++) {
        if (food->position.x == obstacles[i].position.x && food->position.y == obstacles[i].position.y) {
            food->position.x = rand() % (WIDTH / GRID_SIZE);
            food->position.y = rand() % (HEIGHT / GRID_SIZE);
            i = -1; // Recommencer la vérification avec tous les obstacles
        }
    }

    /* Générer une couleur aléatoire pour la nourriture */
    food->color = MLV_rgba(rand() % 256, rand() % 256, rand() % 256, 255);
}

void generate_obstacles(Obstacle* obstacles, int num_obstacles, Snake* snake, Food* food) {
    for (int i = 0; i < num_obstacles; i++) {
        obstacles[i].position.x = rand() % (WIDTH / GRID_SIZE);
        obstacles[i].position.y = rand() % (HEIGHT / GRID_SIZE);

        /* Vérifier que l'obstacle n'apparaît pas sur le serpent, la nourriture ou un autre obstacle */
        while ((obstacles[i].position.x == snake->position.x && obstacles[i].position.y == snake->position.y) ||
               (obstacles[i].position.x == food->position.x && obstacles[i].position.y == food->position.y)) {
            obstacles[i].position.x = rand() % (WIDTH / GRID_SIZE);
            obstacles[i].position.y = rand() % (HEIGHT / GRID_SIZE);
        }

        for (int j = 0; j < i; j++) {
            if (obstacles[i].position.x == obstacles[j].position.x && obstacles[i].position.y == obstacles[j].position.y) {
                obstacles[i].position.x = rand() % (WIDTH / GRID_SIZE);
                obstacles[i].position.y = rand() % (HEIGHT / GRID_SIZE);
                j = -1; // Recommencer la vérification avec tous les obstacles précédents
            }
        }

        /* Générer une couleur aléatoire pour l'obstacle */
        obstacles[i].color = MLV_rgba(128, 128, 128, 255); // Gris
    }
}

int main() {
    Snake snake;
    Direction direction = RIGHT;
    Food food;
    Obstacle obstacles[5];
    int num_obstacles = 5;

    snake.position.x = WIDTH / (2 * GRID_SIZE);
    snake.position.y = HEIGHT / (2 * GRID_SIZE);
    snake.size = 0;

    MLV_create_window("Snake", "Snake", WIDTH, HEIGHT);

    srand(time(NULL));

    generate_food(&food, &snake, obstacles, num_obstacles);
    generate_obstacles(obstacles, num_obstacles, &snake, &food);

    while (1) {
        MLV_clear_window(MLV_COLOR_BLACK);

        /* Dessiner le serpent, la nourriture et les obstacles */
        draw_snake(&snake);
        draw_food(&food);
        for (int i = 0; i < num_obstacles; i++) {
            draw_obstacle(&obstacles[i]);
        }

        /* Mettre à jour la fenêtre graphique */
        MLV_actualise_window();

        /* Vérifier les événements de clavier */
        if (MLV_is_keyboard_arrow()) {
            MLV_Keyboard_button arrow = MLV_get_keyboard_arrow();
            if (arrow == MLV_KEYBOARD_UP) {
                direction = UP;
            } else if (arrow == MLV_KEYBOARD_DOWN) {
                direction = DOWN;
            } else if (arrow == MLV_KEYBOARD_LEFT) {
                direction = LEFT;
            } else if (arrow == MLV_KEYBOARD_RIGHT) {
                direction = RIGHT;
            }
        }

        /* Déplacer le serpent */
        move_snake(&snake, direction);

        /* Gérer les collisions */
        int collision = check_collision(&snake, &food, obstacles, num_obstacles);
        if (collision == 1) {
            break; // Collision avec les bords, le corps du serpent ou un obstacle
        } else if (collision == 2) {
            snake.size++;
            if (snake.size > MAX_SNAKE_SIZE) {
                snake.size = MAX_SNAKE_SIZE;
            }
            generate_food(&food, &snake, obstacles, num_obstacles);
        }

        /* Attendre un court instant */
        MLV_wait_milliseconds(100);
    }

    MLV_free_window();

    return 0;
}
