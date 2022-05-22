
create table especialidad (
id_especialidad int not null generated always as identity,
nombre_esp varchar(60) not null, 
activa boolean default true,
primary key (id_especialidad)
);

create table paciente (
id_pac int not null generated always as identity,
nombre varchar(70), 
clave_pac varchar(30),
primary key (id_pac)
);

create table doctor (
id_doctor int not null generated always as identity, 
nom_doc varchar(70),
usuario varchar (30), 
hash_pass varchar(120),
admin boolean default false,
id_especialidad int not null,
activo boolean default true,
primary key (id_doctor),
foreign key (id_especialidad) references especialidad (id_especialidad) on delete no action
);

create table insight(
id_insight int not null generated always as identity, 
id_doctor int not null,
id_pac int not null,
comentario varchar (750) , 
primary key (id_insight),
foreign key (id_doctor) references doctor (id_doctor) on delete no action,
foreign key (id_pac) references paciente (id_pac) on delete no action 
);

create table permisos(
id_permiso int not null generated always as identity ,
id_doctor int not null, 
id_pac int not null, 
id_especialidad int not null,
activo boolean default true,
primary key (id_permiso),
foreign key (id_pac) references paciente (id_pac) on delete no action,
foreign key (id_doctor) references doctor (id_doctor) on delete no action ,
foreign key (id_especialidad) references especialidad (id_especialidad) on delete no action 
);


CREATE TYPE tipos_input AS ENUM ('number', 'text', 'date','radio','select','check','check/text');

create table pregunta(
id_preg int not null generated always as identity ,
id_especialidad int not null,
pregunta varchar (80) not null,
tipo tipos_input not null,
primary key (id_preg),
foreign  key (id_especialidad) references especialidad (id_especialidad) on delete no action 
);



create table preg_pac (
id_preg_pac int not null generated always as identity ,
id_preg int not null, 
id_pac int not null,
primary key (id_preg_pac),
foreign key (id_preg) references pregunta (id_preg) on delete  no action ,
foreign key (id_pac) references paciente (id_pac) on delete no action 
);



create table resp_abierta (
id_resp_preg_pac int not null generated always as identity ,
id_preg_pac int not null, 
resp_preg varchar(100) not null,
primary key (id_resp_preg_pac), 
foreign key (id_preg_pac) references preg_pac (id_preg_pac) on delete no action 
);

create table opc_preg(
id_opc_preg int not null generated always as identity, 
id_preg int not null, 
resp_opc_preg varchar (100) not null, 
primary key (id_opc_preg),
foreign key (id_preg) references pregunta (id_preg)
);

create table res_preg_opc (
id_resp_preg_opc int not null generated always as identity, 
id_preg_pac int not null, 
id_opc_preg  int not null, 
primary key (id_resp_preg_opc),
foreign key (id_preg_pac) references preg_pac (id_preg_pac) on delete no action ,
foreign key (id_opc_preg) references opc_preg (id_opc_preg) on delete no action 
);