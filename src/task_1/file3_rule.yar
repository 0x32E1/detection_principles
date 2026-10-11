rule file3_bin_unique
{
	meta:
		description = "Detects file3.bin"
		author = "Abdur-Rashid"

	strings: 
		$text1 = "Malware_C_Signature" ascii
		$hex1 = { 73ac 550c 3afc }
	condition:
		$text1 and $hex1
}
