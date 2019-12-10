
INSERT INTO `demandai_administrador_content`(`id`, `model`, `name`, `icon`) VALUES
    (1 ,'demand', 'Demandas', 'fa fa-newspaper'),
    (2, 'prospeccao', 'Prospecção', 'mdi mdi-receipt'),
    (3, 'service', 'Serviços', 'fa fa-suitcase'),
    (4, 'laboratory', 'Laboratorios', 'fa fa-lightbulb'),
    (5, 'equipament', 'Equipamentos', 'fa fa-cogs'),
    (6 ,'institution', 'Instituições', 'fa fa-university'),
    (7, 'profile', 'Usuarios', 'fa fa-user'),
    (8, 'permission', 'Permissões', 'fa fa-lock');

INSERT INTO `demandai_administrador_permission`(`codigo`, `name`, `content_id`) VALUES

        ('add_laboratory', 'Adicionar Laboratório', 4),
        ('update_laboratory', 'Atualizar Laboratório', 4),
        ('delete_laboratory', 'Deletar Laboratório', 4),

        ('add_service', 'Adicionar Serviço', 3),
        ('update_service', 'Atualizar Serviço', 3),
        ('delete_service', 'Deletar Serviço', 3),

        ('add_equipament', 'Adicionar Equipamento', 5),
        ('update_equipament', 'Atualizar Equipamento', 5),
        ('delete_equipament', 'Deletar Equipamento', 5),

        ('add_usuario', 'Adicionar Usuário', 7),
        ('update_usuario', 'Atualizar Usuário', 7),
        ('delete_usuario', 'Deletar Usuário', 7),

        ('add_institution', 'Adicionar Instituição', 6),
        ('update_institution', 'Atualizar Instituição', 6),
        ('delete_institution', 'Deletar Instituição', 6),

        ('prospectar', 'Prospectar', 2),
        ('delete_demand', 'Deletar Demandas', 2),

        ('view_permission', 'Visualizar Permissões', 8),
        ('update_permission', 'Atualizar Permissões', 8),

        ('update_demand', 'Atualizar Demandas', 1);