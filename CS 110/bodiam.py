###
### Author: Derek Tominaga
### Description: Printing Bodiam Castle
###              with adjustable wall size

width = int (input('castle width:\n'))
print ("\n   " + " "*width + ".-.-." + " "*width + "   ")
print ("[-]" + " "*width + "|-.-|" +  " "*width + "[-]")
print ("| |" + "_"*width + "| H |" + "_"*width + "| |")
print ("| |" + " "*width + "| H |" + " "*width + "| |" )
print ("| |" + " "*width + "| H |" + " "*width + "| |")
print ("|_|" + "_"*width + "||^||" + "_"*width + "|_|")