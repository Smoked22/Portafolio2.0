# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdministradorUsuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=16, blank=True, null=True)
    nombre_de_usuario = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador_usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    id_boleta = models.CharField(primary_key=True, max_length=20)
    fecha = models.DateField()
    hora = models.DateField()
    monto = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'boleta'


class Ciudad(models.Model):
    id_ciudad = models.CharField(primary_key=True, max_length=5)
    nom_ciudad = models.CharField(max_length=40)
    comuna_id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    c_rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.CharField(primary_key=True, max_length=5)
    nom_comuna = models.CharField(max_length=40)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleOrden(models.Model):
    comentarios = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField()
    estado_orden = models.CharField(max_length=25)
    orden_id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='orden_id_orden', blank=True, null=True)
    menu_item_id_menuitem = models.ForeignKey('MenuItem', models.DO_NOTHING, db_column='menu_item_id_menuitem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DetalleReceta(models.Model):
    instruccion = models.CharField(max_length=400)
    receta_id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_id_receta', blank=True, null=True)
    ingrediente_id_ingrediente = models.ForeignKey('Ingrediente', models.DO_NOTHING, db_column='ingrediente_id_ingrediente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_receta'


class DetalleReserva(models.Model):
    cant_mesas = models.BigIntegerField()
    estado_reserva = models.CharField(max_length=10)
    mesa_id_mesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='mesa_id_mesa', blank=True, null=True)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)
    cant_personas = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_reserva'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    e_rut = models.BigIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    prim_nom = models.CharField(max_length=30)
    seg_nom = models.CharField(max_length=25, blank=True, null=True)
    prim_apell = models.CharField(max_length=30)
    sec_apell = models.CharField(max_length=25)
    genero = models.CharField(max_length=25)
    telefono = models.BigIntegerField(blank=True, null=True)
    fec_nac = models.CharField(max_length=30)
    salario = models.BigIntegerField()
    rol_empleado_id_rol = models.ForeignKey('RolEmpleado', models.DO_NOTHING, db_column='rol_empleado_id_rol')
    correo = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class GuiaDespacho(models.Model):
    id_envio = models.CharField(primary_key=True, max_length=16)
    tammanio = models.CharField(max_length=15)
    gd_desc = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.CharField(max_length=20)
    u_medida = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    monto_neto = models.CharField(max_length=20)
    iva = models.BigIntegerField()
    total = models.CharField(max_length=12)
    suministro_id_sumplemento = models.ForeignKey('Suministro', models.DO_NOTHING, db_column='suministro_id_sumplemento', blank=True, null=True)
    fec_envio = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_despacho'


class Ingrediente(models.Model):
    id_ingrediente = models.CharField(primary_key=True, max_length=8)
    nom_ingrediente = models.CharField(max_length=40)
    i_desc = models.CharField(max_length=60)
    stock = models.BigIntegerField()
    unidad_de_medida = models.CharField(max_length=20)
    guia_despacho_id_envio = models.ForeignKey(GuiaDespacho, models.DO_NOTHING, db_column='guia_despacho_id_envio', blank=True, null=True)
    fec_caduc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ingrediente'


class Menu(models.Model):
    id_menu = models.CharField(primary_key=True, max_length=6)
    tipo_menu = models.CharField(max_length=30)
    desde = models.DateField()
    hasta = models.DateField()

    class Meta:
        managed = False
        db_table = 'menu'


class MenuItem(models.Model):
    id_menuitem = models.CharField(primary_key=True, max_length=10)
    mi_nombre = models.CharField(max_length=35)
    mi_desc = models.CharField(max_length=80)
    precio = models.CharField(max_length=10)
    tamannio = models.CharField(max_length=20)
    menu_id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu_id_menu', blank=True, null=True)
    receta_id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_id_receta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_item'


class Mesa(models.Model):
    id_mesa = models.CharField(primary_key=True, max_length=5)
    capacidad = models.BigIntegerField()
    estareservada = models.FloatField()
    tieneorden = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mesa'


class Orden(models.Model):
    id_orden = models.CharField(primary_key=True, max_length=16)
    fecha = models.CharField(max_length=16)
    hora = models.CharField(max_length=16)
    mesa_id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='mesa_id_mesa', blank=True, null=True)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta')

    class Meta:
        managed = False
        db_table = 'orden'


class Proveedor(models.Model):
    rut_social = models.CharField(primary_key=True, max_length=18)
    giro = models.CharField(max_length=30, blank=True, null=True)
    p_nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=80)
    p_correo = models.CharField(max_length=80)
    p_telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=60)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad', blank=True, null=True)
    razon_social = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    id_receta = models.CharField(primary_key=True, max_length=6)
    nom_receta = models.CharField(max_length=20)
    porcion = models.CharField(max_length=25)
    r_desc = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'receta'


class Region(models.Model):
    id_region = models.CharField(primary_key=True, max_length=4)
    nom_region = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    id_reserva = models.CharField(primary_key=True, max_length=8)
    fec_reserv_hecha = models.DateField()
    fec_reser = models.DateField()
    empleado_e_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_e_rut', blank=True, null=True)
    cliente_c_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_c_rut')
    origen_reserv = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'reserva'


class RolEmpleado(models.Model):
    id_rol = models.CharField(primary_key=True, max_length=3)
    rol_desc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol_empleado'


class Suministro(models.Model):
    id_suministro = models.CharField(primary_key=True, max_length=12)
    tamannio = models.CharField(max_length=25)
    nombre = models.CharField(max_length=40)
    s_desc = models.CharField(max_length=80, blank=True, null=True)
    proveedor_rut_social = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='proveedor_rut_social', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suministro'


class Transaccion(models.Model):
    id_transaccion = models.CharField(primary_key=True, max_length=20)
    fecha = models.DateField()
    hora = models.DateField()
    tipo_pago = models.CharField(max_length=30)
    monto = models.CharField(max_length=12)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'
