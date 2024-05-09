
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftMULTIPLICATIONDIVISIONCOLON COMMA CTE_FLOAT CTE_INT CTE_STRING DIVISION DO ELSE END EQUAL FLOAT GREATER_THAN ID IF INT LEFT_BRACE LEFT_BRACKET LEFT_PARENTHESIS LESS_THAN MAIN MINUS MULTIPLICATION NOT_EQUAL PLUS PRINT PROGRAM RIGHT_BRACE RIGHT_BRACKET RIGHT_PARENTHESIS SEMICOLON VAR VOID WHILEPROGRAMA : PROGRAM ID SEMICOLON DEC_VARS DEC_FUNCS MAIN BODY ENDDEC_VARS : epsilon\n                | VARSSOLO_FUNCS : FUNCS MAS_FUNCSMAS_FUNCS : epsilon\n                 | SOLO_FUNCSDEC_FUNCS : epsilon\n                 | SOLO_FUNCSVARS : VAR LISTA_VARLISTA_VAR : LISTA_ID COLON TYPE SEMICOLON MAS_VARMAS_VAR : epsilon\n               | LISTA_VARLISTA_ID : ID MAS_IDMAS_ID : COMMA LISTA_ID\n              | epsilonTYPE : INT\n            | FLOATFUNCS : VOID ID LEFT_PARENTHESIS PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNC BODY RIGHT_BRACKET SEMICOLONPARAMETROS : epsilon\n                  | DEC_PARAMETROSDEC_PARAMETROS : ID COLON TYPE LISTA_PARAMETROSLISTA_PARAMETROS : epsilon\n                        | COMMA DEC_PARAMETROSVARS_FUNC : epsilon\n                 | VARSBODY : LEFT_BRACE DEC_STATEMENTS RIGHT_BRACEDEC_STATEMENTS : epsilon\n                      | LISTA_STATEMENTSLISTA_STATEMENTS : STATEMENT MAS_STATEMENTSMAS_STATEMENTS : epsilon\n                      | LISTA_STATEMENTSSTATEMENT : ASSIGN\n                 | CONDITION\n                 | CYCLE\n                 | F_CALL\n                 | PRINT_STMT\n    ASSIGN : ID EQUAL EXPRESION SEMICOLONEXPRESION : EXP MAS_EXPRESIONESMAS_EXPRESIONES : epsilon\n                       | OPERADORES EXPOPERADORES : GREATER_THAN\n                  | LESS_THAN\n                  | NOT_EQUALEXP : TERMINO MAS_EXPMAS_EXP : OPERADORES_EXP EXP\n               | epsilonOPERADORES_EXP : PLUS\n                      | MINUSTERMINO : FACTOR MAS_TERMINOMAS_TERMINO : epsilon\n                   | OPERADORES_TER TERMINOOPERADORES_TER : MULTIPLICATION\n                      | DIVISIONFACTOR : OPERADORES_FACTOR ID_CTE\n              | LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESISID_CTE : ID\n              | CTEOPERADORES_FACTOR : PLUS\n                         | MINUS\n                         | epsilonCTE : CTE_INT\n           | CTE_FLOATCONDITION : IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS BODY ELSE_CONDITIONELSE_CONDITION : epsilon\n                      | ELSE BODYCYCLE : WHILE BODY DO LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS SEMICOLONF_CALL : ID LEFT_PARENTHESIS EXPRESIONES RIGHT_PARENTHESIS SEMICOLONEXPRESIONES : epsilon\n                   | EXPRESIONES_FEXPRESIONES_F : EXPRESION LISTA_EXPLISTA_EXP : epsilon\n                 | COMMA EXPRESIONES_FPRINT_STMT : PRINT LEFT_PARENTHESIS PARAMETROS_PRINT RIGHT_PARENTHESIS SEMICOLONPARAMETROS_PRINT : CTE_STRING MAS_PRINT\n                        | EXPRESION MAS_PRINTMAS_PRINT : epsilon\n                 | COMMA PARAMETROS_PRINTepsilon :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,33,],[0,-1,]),'ID':([2,8,13,24,27,28,37,38,39,40,41,42,51,52,56,57,58,60,70,71,72,73,74,76,86,89,90,91,92,94,96,97,100,101,102,112,114,118,122,130,132,134,138,139,143,144,],[3,16,21,16,43,47,43,-32,-33,-34,-35,-36,16,-26,-78,-78,-78,-78,104,-78,-58,-59,-60,-60,-37,-78,-41,-42,-43,-78,-47,-48,-78,-52,-53,-78,-78,-78,47,-67,-78,-73,-63,-64,-65,-66,]),'SEMICOLON':([3,29,30,31,66,67,68,69,87,88,93,95,98,99,103,104,105,106,107,109,115,126,127,128,129,141,142,],[4,51,-16,-17,86,-78,-78,-78,-38,-39,-44,-46,-49,-50,-54,-56,-57,-61,-62,130,134,-40,-45,-51,-55,144,145,]),'VOID':([4,5,6,7,12,14,51,63,64,65,145,],[-78,13,-2,-3,13,-9,-78,-10,-11,-12,-18,]),'MAIN':([4,5,6,7,9,10,11,12,14,18,19,20,51,63,64,65,145,],[-78,-78,-2,-3,17,-7,-8,-78,-9,-4,-5,-6,-78,-10,-11,-12,-18,]),'VAR':([4,85,],[8,8,]),'LEFT_BRACE':([14,17,45,51,63,64,65,85,113,123,124,125,140,],[-9,27,27,-78,-10,-11,-12,-78,27,27,-24,-25,27,]),'COLON':([15,16,23,25,32,47,],[22,-78,-13,-15,-14,61,]),'COMMA':([16,30,31,67,68,69,78,82,83,84,87,88,93,95,98,99,103,104,105,106,107,126,127,128,129,],[24,-16,-17,-78,-78,-78,112,118,118,122,-38,-39,-44,-46,-49,-50,-54,-56,-57,-61,-62,-40,-45,-51,-55,]),'LEFT_PARENTHESIS':([21,43,44,46,56,57,58,60,71,80,89,90,91,92,94,96,97,100,101,102,112,114,118,],[28,57,58,60,71,71,71,71,71,114,71,-41,-42,-43,71,-47,-48,71,-52,-53,71,71,71,]),'INT':([22,61,],[30,30,]),'FLOAT':([22,61,],[31,31,]),'END':([26,52,],[33,-26,]),'RIGHT_BRACE':([27,34,35,36,37,38,39,40,41,42,52,53,54,55,86,130,132,134,138,139,143,144,],[-78,52,-27,-28,-78,-32,-33,-34,-35,-36,-26,-29,-30,-31,-37,-67,-78,-73,-63,-64,-65,-66,]),'IF':([27,37,38,39,40,41,42,52,86,130,132,134,138,139,143,144,],[44,44,-32,-33,-34,-35,-36,-26,-37,-67,-78,-73,-63,-64,-65,-66,]),'WHILE':([27,37,38,39,40,41,42,52,86,130,132,134,138,139,143,144,],[45,45,-32,-33,-34,-35,-36,-26,-37,-67,-78,-73,-63,-64,-65,-66,]),'PRINT':([27,37,38,39,40,41,42,52,86,130,132,134,138,139,143,144,],[46,46,-32,-33,-34,-35,-36,-26,-37,-67,-78,-73,-63,-64,-65,-66,]),'RIGHT_PARENTHESIS':([28,30,31,48,49,50,57,67,68,69,75,76,77,78,79,81,82,83,84,87,88,93,95,98,99,103,104,105,106,107,108,110,111,116,117,119,120,121,126,127,128,129,131,133,135,136,],[-78,-16,-17,62,-19,-20,-78,-78,-78,-78,109,-68,-69,-78,113,115,-78,-78,-78,-38,-39,-44,-46,-49,-50,-54,-56,-57,-61,-62,129,-70,-71,-74,-76,-75,-21,-22,-40,-45,-51,-55,-72,141,-77,-23,]),'EQUAL':([43,],[56,]),'DO':([52,59,],[-26,80,]),'ELSE':([52,132,],[-26,140,]),'RIGHT_BRACKET':([52,137,],[-26,142,]),'PLUS':([56,57,58,60,68,69,71,89,90,91,92,94,96,97,98,99,100,101,102,103,104,105,106,107,112,114,118,128,129,],[72,72,72,72,96,-78,72,72,-41,-42,-43,72,-47,-48,-49,-50,72,-52,-53,-54,-56,-57,-61,-62,72,72,72,-51,-55,]),'MINUS':([56,57,58,60,68,69,71,89,90,91,92,94,96,97,98,99,100,101,102,103,104,105,106,107,112,114,118,128,129,],[73,73,73,73,97,-78,73,73,-41,-42,-43,73,-47,-48,-49,-50,73,-52,-53,-54,-56,-57,-61,-62,73,73,73,-51,-55,]),'CTE_INT':([56,57,58,60,70,71,72,73,74,76,89,90,91,92,94,96,97,100,101,102,112,114,118,],[-78,-78,-78,-78,106,-78,-58,-59,-60,-60,-78,-41,-42,-43,-78,-47,-48,-78,-52,-53,-78,-78,-78,]),'CTE_FLOAT':([56,57,58,60,70,71,72,73,74,76,89,90,91,92,94,96,97,100,101,102,112,114,118,],[-78,-78,-78,-78,107,-78,-58,-59,-60,-60,-78,-41,-42,-43,-78,-47,-48,-78,-52,-53,-78,-78,-78,]),'CTE_STRING':([60,118,],[82,82,]),'LEFT_BRACKET':([62,],[85,]),'GREATER_THAN':([67,68,69,93,95,98,99,103,104,105,106,107,127,128,129,],[90,-78,-78,-44,-46,-49,-50,-54,-56,-57,-61,-62,-45,-51,-55,]),'LESS_THAN':([67,68,69,93,95,98,99,103,104,105,106,107,127,128,129,],[91,-78,-78,-44,-46,-49,-50,-54,-56,-57,-61,-62,-45,-51,-55,]),'NOT_EQUAL':([67,68,69,93,95,98,99,103,104,105,106,107,127,128,129,],[92,-78,-78,-44,-46,-49,-50,-54,-56,-57,-61,-62,-45,-51,-55,]),'MULTIPLICATION':([69,103,104,105,106,107,129,],[101,-54,-56,-57,-61,-62,-55,]),'DIVISION':([69,103,104,105,106,107,129,],[102,-54,-56,-57,-61,-62,-55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'DEC_VARS':([4,],[5,]),'epsilon':([4,5,12,16,27,28,37,51,56,57,58,60,67,68,69,71,78,82,83,84,85,89,94,100,112,114,118,132,],[6,10,19,25,35,49,54,64,74,76,74,74,88,95,99,74,111,117,117,121,124,74,74,74,74,74,74,139,]),'VARS':([4,85,],[7,125,]),'DEC_FUNCS':([5,],[9,]),'SOLO_FUNCS':([5,12,],[11,20,]),'FUNCS':([5,12,],[12,12,]),'LISTA_VAR':([8,51,],[14,65,]),'LISTA_ID':([8,24,51,],[15,32,15,]),'MAS_FUNCS':([12,],[18,]),'MAS_ID':([16,],[23,]),'BODY':([17,45,113,123,140,],[26,59,132,137,143,]),'TYPE':([22,61,],[29,84,]),'DEC_STATEMENTS':([27,],[34,]),'LISTA_STATEMENTS':([27,37,],[36,55,]),'STATEMENT':([27,37,],[37,37,]),'ASSIGN':([27,37,],[38,38,]),'CONDITION':([27,37,],[39,39,]),'CYCLE':([27,37,],[40,40,]),'F_CALL':([27,37,],[41,41,]),'PRINT_STMT':([27,37,],[42,42,]),'PARAMETROS':([28,],[48,]),'DEC_PARAMETROS':([28,122,],[50,136,]),'MAS_STATEMENTS':([37,],[53,]),'MAS_VAR':([51,],[63,]),'EXPRESION':([56,57,58,60,71,112,114,118,],[66,78,79,83,108,78,133,83,]),'EXP':([56,57,58,60,71,89,94,112,114,118,],[67,67,67,67,67,126,127,67,67,67,]),'TERMINO':([56,57,58,60,71,89,94,100,112,114,118,],[68,68,68,68,68,68,68,128,68,68,68,]),'FACTOR':([56,57,58,60,71,89,94,100,112,114,118,],[69,69,69,69,69,69,69,69,69,69,69,]),'OPERADORES_FACTOR':([56,57,58,60,71,89,94,100,112,114,118,],[70,70,70,70,70,70,70,70,70,70,70,]),'EXPRESIONES':([57,],[75,]),'EXPRESIONES_F':([57,112,],[77,131,]),'PARAMETROS_PRINT':([60,118,],[81,135,]),'MAS_EXPRESIONES':([67,],[87,]),'OPERADORES':([67,],[89,]),'MAS_EXP':([68,],[93,]),'OPERADORES_EXP':([68,],[94,]),'MAS_TERMINO':([69,],[98,]),'OPERADORES_TER':([69,],[100,]),'ID_CTE':([70,],[103,]),'CTE':([70,],[105,]),'LISTA_EXP':([78,],[110,]),'MAS_PRINT':([82,83,],[116,119,]),'LISTA_PARAMETROS':([84,],[120,]),'VARS_FUNC':([85,],[123,]),'ELSE_CONDITION':([132,],[138,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> PROGRAM ID SEMICOLON DEC_VARS DEC_FUNCS MAIN BODY END','PROGRAMA',8,'p_program','parser.py',17),
  ('DEC_VARS -> epsilon','DEC_VARS',1,'p_dec_vars','parser.py',22),
  ('DEC_VARS -> VARS','DEC_VARS',1,'p_dec_vars','parser.py',23),
  ('SOLO_FUNCS -> FUNCS MAS_FUNCS','SOLO_FUNCS',2,'p_solo_funcs','parser.py',31),
  ('MAS_FUNCS -> epsilon','MAS_FUNCS',1,'p_mas_funcs','parser.py',36),
  ('MAS_FUNCS -> SOLO_FUNCS','MAS_FUNCS',1,'p_mas_funcs','parser.py',37),
  ('DEC_FUNCS -> epsilon','DEC_FUNCS',1,'p_dec_funcs','parser.py',45),
  ('DEC_FUNCS -> SOLO_FUNCS','DEC_FUNCS',1,'p_dec_funcs','parser.py',46),
  ('VARS -> VAR LISTA_VAR','VARS',2,'p_vars','parser.py',56),
  ('LISTA_VAR -> LISTA_ID COLON TYPE SEMICOLON MAS_VAR','LISTA_VAR',5,'p_lista_var','parser.py',61),
  ('MAS_VAR -> epsilon','MAS_VAR',1,'p_mas_var','parser.py',66),
  ('MAS_VAR -> LISTA_VAR','MAS_VAR',1,'p_mas_var','parser.py',67),
  ('LISTA_ID -> ID MAS_ID','LISTA_ID',2,'p_lista_id','parser.py',75),
  ('MAS_ID -> COMMA LISTA_ID','MAS_ID',2,'p_mas_id','parser.py',80),
  ('MAS_ID -> epsilon','MAS_ID',1,'p_mas_id','parser.py',81),
  ('TYPE -> INT','TYPE',1,'p_type','parser.py',91),
  ('TYPE -> FLOAT','TYPE',1,'p_type','parser.py',92),
  ('FUNCS -> VOID ID LEFT_PARENTHESIS PARAMETROS RIGHT_PARENTHESIS LEFT_BRACKET VARS_FUNC BODY RIGHT_BRACKET SEMICOLON','FUNCS',10,'p_funcs','parser.py',99),
  ('PARAMETROS -> epsilon','PARAMETROS',1,'p_parametros','parser.py',104),
  ('PARAMETROS -> DEC_PARAMETROS','PARAMETROS',1,'p_parametros','parser.py',105),
  ('DEC_PARAMETROS -> ID COLON TYPE LISTA_PARAMETROS','DEC_PARAMETROS',4,'p_dec_parametros','parser.py',113),
  ('LISTA_PARAMETROS -> epsilon','LISTA_PARAMETROS',1,'p_lista_parametros','parser.py',118),
  ('LISTA_PARAMETROS -> COMMA DEC_PARAMETROS','LISTA_PARAMETROS',2,'p_lista_parametros','parser.py',119),
  ('VARS_FUNC -> epsilon','VARS_FUNC',1,'p_vars_func','parser.py',127),
  ('VARS_FUNC -> VARS','VARS_FUNC',1,'p_vars_func','parser.py',128),
  ('BODY -> LEFT_BRACE DEC_STATEMENTS RIGHT_BRACE','BODY',3,'p_body','parser.py',138),
  ('DEC_STATEMENTS -> epsilon','DEC_STATEMENTS',1,'p_dec_staments','parser.py',143),
  ('DEC_STATEMENTS -> LISTA_STATEMENTS','DEC_STATEMENTS',1,'p_dec_staments','parser.py',144),
  ('LISTA_STATEMENTS -> STATEMENT MAS_STATEMENTS','LISTA_STATEMENTS',2,'p_lista_staments','parser.py',152),
  ('MAS_STATEMENTS -> epsilon','MAS_STATEMENTS',1,'p_mas_staments','parser.py',157),
  ('MAS_STATEMENTS -> LISTA_STATEMENTS','MAS_STATEMENTS',1,'p_mas_staments','parser.py',158),
  ('STATEMENT -> ASSIGN','STATEMENT',1,'p_statement','parser.py',168),
  ('STATEMENT -> CONDITION','STATEMENT',1,'p_statement','parser.py',169),
  ('STATEMENT -> CYCLE','STATEMENT',1,'p_statement','parser.py',170),
  ('STATEMENT -> F_CALL','STATEMENT',1,'p_statement','parser.py',171),
  ('STATEMENT -> PRINT_STMT','STATEMENT',1,'p_statement','parser.py',172),
  ('ASSIGN -> ID EQUAL EXPRESION SEMICOLON','ASSIGN',4,'p_assign','parser.py',180),
  ('EXPRESION -> EXP MAS_EXPRESIONES','EXPRESION',2,'p_expresion','parser.py',187),
  ('MAS_EXPRESIONES -> epsilon','MAS_EXPRESIONES',1,'p_mas_expresiones','parser.py',192),
  ('MAS_EXPRESIONES -> OPERADORES EXP','MAS_EXPRESIONES',2,'p_mas_expresiones','parser.py',193),
  ('OPERADORES -> GREATER_THAN','OPERADORES',1,'p_operadores','parser.py',201),
  ('OPERADORES -> LESS_THAN','OPERADORES',1,'p_operadores','parser.py',202),
  ('OPERADORES -> NOT_EQUAL','OPERADORES',1,'p_operadores','parser.py',203),
  ('EXP -> TERMINO MAS_EXP','EXP',2,'p_exp','parser.py',210),
  ('MAS_EXP -> OPERADORES_EXP EXP','MAS_EXP',2,'p_mas_exp','parser.py',215),
  ('MAS_EXP -> epsilon','MAS_EXP',1,'p_mas_exp','parser.py',216),
  ('OPERADORES_EXP -> PLUS','OPERADORES_EXP',1,'p_operadores_exp','parser.py',224),
  ('OPERADORES_EXP -> MINUS','OPERADORES_EXP',1,'p_operadores_exp','parser.py',225),
  ('TERMINO -> FACTOR MAS_TERMINO','TERMINO',2,'p_termino','parser.py',232),
  ('MAS_TERMINO -> epsilon','MAS_TERMINO',1,'p_mas_termino','parser.py',237),
  ('MAS_TERMINO -> OPERADORES_TER TERMINO','MAS_TERMINO',2,'p_mas_termino','parser.py',238),
  ('OPERADORES_TER -> MULTIPLICATION','OPERADORES_TER',1,'p_operadores_ter','parser.py',246),
  ('OPERADORES_TER -> DIVISION','OPERADORES_TER',1,'p_operadores_ter','parser.py',247),
  ('FACTOR -> OPERADORES_FACTOR ID_CTE','FACTOR',2,'p_factor','parser.py',254),
  ('FACTOR -> LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS','FACTOR',3,'p_factor','parser.py',255),
  ('ID_CTE -> ID','ID_CTE',1,'p_id_cte','parser.py',263),
  ('ID_CTE -> CTE','ID_CTE',1,'p_id_cte','parser.py',264),
  ('OPERADORES_FACTOR -> PLUS','OPERADORES_FACTOR',1,'p_operadores_factor','parser.py',269),
  ('OPERADORES_FACTOR -> MINUS','OPERADORES_FACTOR',1,'p_operadores_factor','parser.py',270),
  ('OPERADORES_FACTOR -> epsilon','OPERADORES_FACTOR',1,'p_operadores_factor','parser.py',271),
  ('CTE -> CTE_INT','CTE',1,'p_cte','parser.py',281),
  ('CTE -> CTE_FLOAT','CTE',1,'p_cte','parser.py',282),
  ('CONDITION -> IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS BODY ELSE_CONDITION','CONDITION',6,'p_condition','parser.py',289),
  ('ELSE_CONDITION -> epsilon','ELSE_CONDITION',1,'p_else','parser.py',294),
  ('ELSE_CONDITION -> ELSE BODY','ELSE_CONDITION',2,'p_else','parser.py',295),
  ('CYCLE -> WHILE BODY DO LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS SEMICOLON','CYCLE',7,'p_cycle','parser.py',305),
  ('F_CALL -> ID LEFT_PARENTHESIS EXPRESIONES RIGHT_PARENTHESIS SEMICOLON','F_CALL',5,'p_f_call','parser.py',312),
  ('EXPRESIONES -> epsilon','EXPRESIONES',1,'p_expresiones','parser.py',317),
  ('EXPRESIONES -> EXPRESIONES_F','EXPRESIONES',1,'p_expresiones','parser.py',318),
  ('EXPRESIONES_F -> EXPRESION LISTA_EXP','EXPRESIONES_F',2,'p_expresiones_f','parser.py',326),
  ('LISTA_EXP -> epsilon','LISTA_EXP',1,'p_lista_exp','parser.py',331),
  ('LISTA_EXP -> COMMA EXPRESIONES_F','LISTA_EXP',2,'p_lista_exp','parser.py',332),
  ('PRINT_STMT -> PRINT LEFT_PARENTHESIS PARAMETROS_PRINT RIGHT_PARENTHESIS SEMICOLON','PRINT_STMT',5,'p_print_stmt','parser.py',342),
  ('PARAMETROS_PRINT -> CTE_STRING MAS_PRINT','PARAMETROS_PRINT',2,'p_parametros_print','parser.py',347),
  ('PARAMETROS_PRINT -> EXPRESION MAS_PRINT','PARAMETROS_PRINT',2,'p_parametros_print','parser.py',348),
  ('MAS_PRINT -> epsilon','MAS_PRINT',1,'p_mas_print','parser.py',353),
  ('MAS_PRINT -> COMMA PARAMETROS_PRINT','MAS_PRINT',2,'p_mas_print','parser.py',354),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','parser.py',362),
]
