#this is the source code

########################
#CONSTANTS
########################
Digits = '0123456789'
escHars = ';'
#Chars = 'nil' is this needed?
#######################
#ERRORS
#######################

class Error:
  
    def __init__(self, pos_start, pos_end, error_name, status):#all these are args including dets(status). 
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name#get is an arg
        self.status = status
    
    def as_string(self):#gotta remember these are methods
        result = f'{self.error_name}: {self.details}'#should return the error name: details
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'#ln fn in pos but we gone see how it calls
        return result#with no args its more of an "alerter"

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, status):#this an super__init__frm Error/
        super().__init__('Illegal Character', stuatus)#this is one way to make statuses

########################
# POSITION
########################

class Pos: # POSITION
  
    def __init__(self, idx, ln, col, fn, ftxt):#Posistion pos.(-1arg,0arg,-1arg,fn,ftxt)
        self.idx  = idx#idkfully
        self.ln = ln 
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def adv(self, current_char):
        self.idx += 1
        self.col += 1#see if i can make indt

    def Indt(self):#std ind
#dnt touch ln
        self.idx +=1
        self.col +=4
        self.ln +=1

        if current_char == '\n':
            self.ln += 1 
            self.col = 0

        return self
    
    def cpy(self):#this sum how a cpy think it catch char and const
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#########################
# TOKENS
##########################
#* Constants for TOKENS
# TT stands for token type

TT_SEMICOLON = ';' #; jus bc
TT_INT = 'TT_INT'#0123456789
TT_FLOAT = 'FLOAT'#.00001
TT_PLUS = 'PLUS'# + 
TT_MINUS = 'MINUS'# - 
TT_MUL = 'MUL'# * 
TT_DIV = 'DIV'# / 
TT_LPAREN = 'LPAREN'# ( 
TT_RPAREN = 'RPAREN'# )

class Tokens:
    def __init__(self,type_,value = None):
        self.type = type_#wrkn on tokens, also tokens like [] is considered a token
        self.value = value#needed for skel wrk

    def __repr__(self):#enforces str/char
        if self.value: return f'{self.type}:{self.value}'#if token has a value it will print the 'type:value'
        return f'{self.type}'#if it doesnt have a value it will print jus the type, weird dict type

############################
#LEXER
############################

class Lexer:#this is what read the text
    
    def __init__(self,fn, text):
        self.fn = fn
        self.text = text #this makes text and obj of lexer
        self.pos = Position(-1, 0, -1, fn, text)#make sure it doesnt start at a blank space and the code starts to freak out
        self.current_char = None#agains sets everything basically to 0 or -1
        self.adv()

    def adv(self):
        self.pos.adv(self.current_char)
        #below is where the lexer will advance but what stops it from being an infinite loop is the else None
        # current char is linked with adv. and is equal to the pos of the text. 
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None 

    def make_tokens(self):
        #tokens take array data bytes... gotta read docs
        tokens = []

        while self.current_char != None:#not empy bits
            if self.current_char in '\n':#this will check for blank spaces and move on
                self.adv()#treat it like enter
            elif self.current_char in escHars:
                tokens.append(self.make_escape())
                self.adv()
            elif self.current_char == ';':
                tokens.append(Tokens(TT_SEMICOLON))
                self.Indt()
                elif:# the error this should fuck the jedi up
                    pos_start = self.pos.copy()
                    char = self.current_char
                    self.adv()
                    return [], IllegalCharError(pos_start, self.pos,"' " + char +" '")#char the actualy string  
            
            elif self.current_char in Digits:#feel like math gone get done btw cmd and servo
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))#i might have to call it tokens(remember to add the S)
                self.adv()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.adv()
            else:# the error
                pos_start = self.pos.copy()
                char = self.current_char
                self.adv()
                return [], IllegalCharError(pos_start, self.pos,"' " + char +" '")

        return tokens, None
#yall can see why i rarely homemade or compiled inspired pjs
 def make_number(self):#make the lang aware of yo picky self wanting numbers
        num_str = ''#starts blanks 
        dot_count = 0#dots...

        while self.current_char != None and self.current_char in Digits + '.':#this is more for math which is a great sec check
    #play with yo sec settings is now a new test...make sense soon
            if self.current_char == '.':
                if dot_count == 1: break #ok imp syntax
                dot_count += 1
                num_str += '.'#tied to dots
            else:
                num_str += self.current_char#parse fwd
                self.adv()
            
        if dot_count == 0:#
            return Tokens(TT_INT, int(num_str))#number version of dot count a number str
        else:
            return Tokens(TT_FLOAT, float(num_str))#retn float if its not 0

###########################
#NUMBER NODE
############################

class NumberNode:#nodes needed to parse
    def __init__(self, tok):
        self.tok = tok
    def __repr__(self):
        return f"{self.tok}"#rtn tok as str

class BinOpNode:
    def __init__(self, lft_node,op_tok, rgt_node):
        self.lft_node = lft_node
        self.op_tok = op_tok
        self.rgt_node = rgt_node
    
    def __repr__(self):
        return f'({self.lft_node}, {op_tok}, {rgt_node})'

