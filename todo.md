# TODO List

- [x] initialisation git
- [x] fonction isPrefix(u,v)
  - [x] tester pour chaque caractere de v si u est son prefixe
    - [x] -1 non prefix , 0 egales , 1 prefix
- [x] fonction residuel( M , L)
  - [x] residuels = null ( avec valeurs uniques , pas de doublons)
  - [x] pour chaque elemet u de M on verifie si c'est un residuel
    - [x] on fait le test residuel pour chaque element v de L
      - [x] si isPrefix(u,v) == 1 on ajoute u dans residuels
      - [x] si isPrefix(u,v) == 0 on ajoute '' dans residuels
- [x] fonction anlayse_code_language(L)
  - [x] L_esiduels = [ ]
  - [x] L_[0] = L
  - [x] L_[1] = residuel ( L , L) - ('')
  - [x] pour i partant de 2
    - [x] L_[i] = residuel( L , L_[i-1] ) + residuel(L_[i-1],L)
