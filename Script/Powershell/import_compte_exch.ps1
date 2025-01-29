#On ajoute les fonctionnalités Exchange Management Shell
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn; 

# On fixe sur quelle base de donnée "SMRD" ou "SE2M"
#$dbmailbox= "SMRD"
$dbmailbox= "SE2M"
#On import le fichier CSV
# l'encodage doit être en UTF8 (par défaut)
Import-Csv -Path "C:\Scripts\SE2M\SE2MTech-mailbox.csv" -Delimiter ";" -Encoding Default | foreach {
 # list des champs exploitable : Get-Mailbox testuser1 | fl
 # new-mailbox créer le compte ad avec la boite exch
 $mbox=New-Mailbox -Name ($_.FirstName + ' ' + $_.LastName) -UserPrincipalName $_.EmailAddress -Password (ConvertTo-SecureString $_.PW  -AsPlainText -Force) -FirstName $_.Firstname -LastName $_.LastName -OrganizationalUnit $_.OrganizationnalUnit -Database $dbmailbox
 
# fixe la description dans son compte AD associé s'il y en une
if ($_.Description -ne $null){
$dn = "LDAP://" + $mbox.distinguishedname; 
$obj = [ADSI]$dn
$obj.Description = $_.Description
$obj.setinfo()
                              }
# le mot de passe n'expire jamais
# on fixera plus tard le delai d'expiration par gpo
Set-ADUser -Identity $_.SAN -PasswordNeverExpires $true




 # test affiche champ LastName
 #Write-Host $_.LastName "OK"
 }

 
