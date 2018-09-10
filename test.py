import scrub_dob_util
import scrub_file

str = "[2018-04-19 12:58:59.127812] LOB='M' City='Bellmore' Last='Adams' PCP_Name='Howell, Sarah' Zip='11710' DOB='' Gender='1' Address2='' Phone1='(516) 794-9644' PCP_NPI='111111111' State='NY' TIN='121212121' ApplyMonth='201801' Address1='5 Harvard St. ' Identifier='68D8867BDDCF97FB' TIN_Name='Local Care MDs' First='Aiden'"
print(scrub_dob_util.scrub_line(str))

str = "[2018-04-19 12:58:59.209213] LOB='M' City='Whitestone' Last='Hunt' PCP_Name='Hoffman, Daniel' Zip='11357' DOB='1934-09-23' Gender='1' Address2='' Phone1='(718) 312-2055' PCP_NPI='666666666' State='NY' TIN='343434343' ApplyMonth='201801' Address1='63 Wagon Lane ' Identifier='CDAA63D649FC07FC' TIN_Name='Hoffman Medical Associates' First='Henry'"
print(scrub_dob_util.scrub_line(str))

#str = "[2018-04-19 12:58:59.208993] LOB='M' City='Amityville' Last='Hunt' PCP_Name='Franklin, Matthew' Zip='11701' Gender='2' Address2='' Phone1='(631) 084-1553' PCP_NPI='222222222' State='NY' TIN='121212121' ApplyMonth='201801' Address1='152 South Ave. ' Identifier='584708A8E06C7260' TIN_Name='Local Care MDs' First='Emma'"
str = "[2018-04-19 12:58:59.209394] LOB='M' City='Schenectady' Last='Hunt' PCP_Name='Hoffman, Daniel' Zip='12302' DOB='X/X/1931' Gender='1' Address2='' Phone1='(518) 653-6397' PCP_NPI='666666666' State='NY' TIN='343434343' ApplyMonth='201801' Address1='7130 53rd Avenue ' Identifier='EE704F8F6E526B37' TIN_Name='Hoffman Medical Associates' First='James'"
print(scrub_dob_util.scrub_line(str))

#scrub_file.write_scrubbed_file()

#scrub_file.download_file()
