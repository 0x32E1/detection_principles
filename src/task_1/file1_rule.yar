rule file1_bin_unique
{
	meta:
		description = "Detects file1.bin"
		author = "Abdur-Rashid"
	
	strings:
		$text1 = "Malware_A_Signature" ascii
		$hex1 = { 64de 731f 9d0c }
	
	condition:
		$text1 and $hex1
}
