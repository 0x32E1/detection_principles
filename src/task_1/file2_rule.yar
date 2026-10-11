rule file2_bin_unique
{
	strings:
		$text1 = "Malware_B_Signature" ascii
		$hex1 = { 1c3d d862 3990 }

	condition:
		filesize == 512027 and $text1 and $hex1
}
