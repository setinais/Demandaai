
INSERT INTO `demandai_administrador_content`(`id`, `model`, `name`) VALUES
    (1, 'prospeccao', 'Prospecção'),
    (2, 'service', 'Serviços'),
    (3, 'laboratory', 'Laboratorios'),
    (4, 'equipament', 'Equipamentos'),
    (5, 'profile', 'Usuarios'),
    (6 ,'institution', 'Instituições'),
    (7, 'permission', 'Permissões');

INSERT INTO `demandai_administrador_permission`(`codigo`, `name`, `content_id`) VALUES

        ('add_laboratory', 'Adicionar Laboratorio', 3),
        ('update_laboratory', 'Atualizar Laboratorio', 3),
        ('delete_laboratory', 'Deletar Laboratorio', 3),

        ('add_service', 'Adicionar Serviço', 2),
        ('update_service', 'Atualizar Serviço', 2),
        ('delete_service', 'Deletar Serviço', 2),

        ('add_equipament', 'Adicionar Equipamento', 4),
        ('update_equipament', 'Atualizar Equipamento', 4),
        ('delete_equipament', 'Deletar Equipamento', 4),

        ('add_usuario', 'Adicionar Usuario', 5),
        ('update_usuario', 'Atualizar Usuario', 5),
        ('delete_usuario', 'Deletar Usuario', 5),

        ('add_institution', 'Adicionar Instituição', 6),
        ('update_institution', 'Atualizar Instituição', 6),
        ('delete_institution', 'Deletar Instituição', 6),

        ('prospectar', 'Prospectar', 1),
        ('view_demand', 'Listar Demandas', 1),
        ('update_demand', 'Atualizar Demandas', 1),
        ('delete_demand', 'Deletar Demandas', 1),

        ('view_permission', 'Listar Permissões', 7),
        ('update_permission', 'Atualizar Permissões', 7),