from typing import List, Dict
from db import ConexaoBD

class ValidacaoUsuario:

  @staticmethod
  def valida_user(email, senha)->str:
    usuario = dict[email, senha]
    user_bd = ConexaoBD.select_user()
    for usuario in user_bd:
      if usuario[email] in user_bd["email"] and usuario[senha] == user_bd["senha"]:
        return("Validacao OK")
      else:
        return("Usuário não validado")

