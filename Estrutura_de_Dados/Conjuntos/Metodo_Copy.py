#Gera um cópia do conjunto

# Permissões padrão para todos os usuários
permissoes_padrao = {"ler", "comentar"}

# Queremos dar permissões extras para administradores
permissoes_admin = permissoes_padrao.copy()
permissoes_admin.add("editar")
permissoes_admin.add("excluir")

# Verificando
print("Permissões padrão:", permissoes_padrao)
print("Permissões admin:", permissoes_admin)