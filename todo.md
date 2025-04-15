# TODO List

- [x] initialisation git
- [x] fonction isPrefix(u,v)
  - [x] tester pour chaque caractere de v si u est son prefixe
    - [x] -1 non prefix , 0 egales , 1 prefix
- [ ] fonction residuel( M , L)
  - [ ] residuels = null ( avec valeurs uniques , pas de doublons)
  - [ ] pour chaque elemet u de M on verifie si c'est un residuel
    - [ ] on fait le test residuel pour chaque element v de L
      - [ ] si isPrefix(u,v) == 1 on ajoute u dans residuels
      - [ ] si isPrefix(u,v) == 0 on ajoute '' dans residuels
- [ ] fonction anlayse_code_language(L)
  - [ ] L_esiduels = []
  - [ ] L_[0] = L
  - [ ] L_[1] = residuel ( L , L) - ('')
  - [ ] pour i partant de 2
    - [ ] L_[i] = residuel( L , L_[i-1] ) + residuel(L_[i-1],L)
