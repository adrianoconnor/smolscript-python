from .expression import Expression
from internals.token import Token

class AssignExpression(Expression):

    def __init__(self, name:Token, value:Expression):
        self.name:Token = name
        self.value:Expression = value

    def accept(self, visitor):
        return visitor.visitAssignExpression(self)
    