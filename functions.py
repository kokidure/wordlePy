def checkWord (input, target):
    result = ""

    if len(input) != 5:
        result = "Debes ingresar una palabra de 5 letras." 
        return (result)

    for i in range(len(input)):
        if input[i] in target:
            if target.rfind(input[i]) == input.rfind(input[i]):
                result = result + "{" + input[i] + "}"
            else:
                result = result + "(" + input[i] + ")"
        else:
            result = result + input[i]
    
    return result