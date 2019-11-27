
INSERT INTO `demandai_administrador_content`(`id`, `model`, `name`) VALUES
    (1, 'laboratory', 'Laboratorios'),
    (2, 'service', 'Serviços'),
    (3, 'equipament', 'Equipamentos'),
    (4, 'usuario', 'Usuarios'),
    (5 ,'institution', 'Instituições'),
    (6, 'prospeccao', 'Prospecção'),
    (7, 'permission', 'Permissões');

INSERT INTO `demandai_administrador_permission`(`codigo`, `name`, `content_id`) VALUES

        ('add_laboratory', 'Adicionar Laboratorio', 1),
        ('view_laboratory', 'Listar Laboratorio', 1),
        ('update_laboratory', 'Atualizar Laboratorio', 1),
        ('delete_laboratory', 'Deletar Laboratorio', 1),

        ('add_service', 'Adicionar Serviço', 2),
        ('view_service', 'Listar Serviço', 2),
        ('update_service', 'Atualizar Serviço', 2),
        ('delete_service', 'Deletar Serviço', 2),

        ('add_equipament', 'Adicionar Equipamento', 3),
        ('view_equipament', 'Listar Equipamento', 3),
        ('update_equipament', 'Atualizar Equipamento', 3),
        ('delete_equipament', 'Deletar Equipamento', 3),

        ('add_usuario', 'Adicionar Usuario', 4),
        ('view_usuario', 'Listar Usuario', 4),
        ('update_usuario', 'Atualizar Usuario', 4),
        ('delete_usuario', 'Deletar Usuario', 4),

        ('add_institution', 'Adicionar Instituição', 5),
        ('view_institution', 'Listar Instituição', 5),
        ('update_institution', 'Atualizar Instituição', 5),
        ('delete_institution', 'Deletar Instituição', 5),

        ('prospectar', 'Adicionar Instituição', 6),
        ('view_demand', 'Listar Instituição', 6),
        ('update_demand', 'Atualizar Instituição', 6),
        ('delete_demand', 'Deletar Instituição', 6),

        ('view_permission', 'Listar Instituição', 7),
        ('update_permission', 'Atualizar Instituição', 7),
        ('delete_institution', 'Deletar Instituição', 7);