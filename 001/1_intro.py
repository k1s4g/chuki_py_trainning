
l_reponse = {  }
l_reponse[ "BIEN" ] = [ "oui","ui", "yes", "good", "bien" ]
l_reponse[ "MAL" ] = [ "non", "mal", "bad", "merde", "pas" ]
user_state = ""
rep = ""

print( "salut chouki!  comment Ca va ? [Bien[/Ou/]Pas]" )
rep = str( raw_input( ":" ) ).lower(  )
print( rep )
print( "-----" )

for i in l_reponse:
    if rep in l_reponse[ i ] :
        user_state = i

if user_state == "" :
    print( "L'utilisateur fait de la retention d'info ! " )
else:
    print( "L'utilisateur ce porte :" + user_state )
        
