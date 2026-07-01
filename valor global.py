GLOBAL_VAR = 'valor global'

def exemplo_local():
    #varial local - só existe dentro desta função
    local_var = 'valor local'
    print('local_var:', local_var)

    #acessar variável global para leitura funcionar sem declarar 'global'
    print('GLOBAL_VAR:', GLOBAL_VAR)

    #usar um built-in (len)
    print('Built-in len(\'abc\'):', len('abc'))

def exemplo_modifica():
    #para modificar a variável global dentro da função, declarar 'global'
    global GLOBAL_VAR
    GLOBAL_VAR = 'novo valor global'
    print('GLOBAL_VAR modificado para:', GLOBAL_VAR)

print('GLOBAL_VAR (antes):', GLOBAL_VAR)
exemplo_local()
exemplo_modifica()
print('GLOBAL_VAR (depois):', GLOBAL_VAR)