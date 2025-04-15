# TODO List

- [x] initialisation git
- [ ] fonction isPrefix(u,v)
  - [ ] tester pour chaque caractere de v si u est son prefixe 
    - [ ] -1 non prefix , 0 egales , 1 prefix
- [ ] fonction residuel( M , L)
  - [ ] pour chaque elemet de M on verifie si c'est un residuel
    - [ ] on fait le test residuel pour chaque element de L
- [ ] fonction anlayse_code_language(L)
  - [ ] L_esiduels = []
  - [ ] L_[0] = L
  - [ ] L_[1] = residuel ( L , L) - ('')
  - [ ] pour i partant de 2
    - [ ] L_[i] = residuel( L , L_[i-1] ) + residuel(L_[i-1],L)
