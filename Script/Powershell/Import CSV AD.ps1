$CSV = Import-CSV Nomdufichier.csv

foreach ($user in $CSV)
{
	$UserName = "$($user.'First Name').$($user.'Last Name')"
	$UserName = $UserName.Replace(" ", "")

$SecurePassword = ConvertTo-SecureString "Motdepasse" -AsPlainText -Force

New-ADUser	-Name "$($user.'First Name') $($user.'Last Name')" `
		-GivenName $user.'First Name' `
		-Surname $user.'Last Name' `
		-UserPrincipalName $User.'UPN' `
		-SamAccountName $User.'SAN' `
		-EmailAddress $User.'Email Address' `
		-Description "$($user.Description)" `
		-Path "$($user.'Organizationnal Unit')" `
		-ChangePasswordAtLogon $true `
		-AccountPassword $SecurePassword `
		-Enabled $user.Enabled
}
