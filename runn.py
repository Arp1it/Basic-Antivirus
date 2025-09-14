import antivirr as antivirr


antivirr.initialize_db()
# virusess = antivirr.deep_scan("C:/")
virusess = antivirr.deep_scan("C:\\Users\\Microsoft\\Documents\\prrrog\\cybersecurityprotection")
# print(virusess)

# with open("virusesssss.txt", "w+") as f:
#     for i in virusess:
#         f.write(str(i) + "\n")

# junkfiles = antivirr.junk_cleaner()
# print(junkfiles)

rambooster = antivirr.ram_booster()

antivirr.close_db()