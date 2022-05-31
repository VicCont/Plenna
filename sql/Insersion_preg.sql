drop table IF EXISTS auxiliar ;

create temp table auxiliar(
id int not null generated always as identity,
categoria varchar(100),
pregunta varchar (100),
tipo varchar (100),
nota varchar(60),
valor varchar (100),
primary key (id)
);

COPY auxiliar (categoria ,pregunta, tipo, nota, valor)
FROM '/home/ubuntu/plenna/insertable.csv'
DELIMITER '|'
CSV header encoding 'latin1';


insert into especialidad (nombre_esp)
select distinct on (categoria) categoria from auxiliar   ;

insert into pregunta (id_especialidad ,pregunta ,tipo )
select id_especialidad, pregunta ,prueba::tipos_input 
  from(
	select distinct on (pregunta) pregunta,id_especialidad ,nombre_esp, 
	case 
		when tipo ='Si/ No' then 'radio'
		when tipo='Número' then 'number'
		when tipo='Texto' then 'text'
		when tipo='select' then 'select'
		when tipo='Opción múltiple' then 'check'
		when tipo='Opción múltiple/input' then 'check/text'
		when tipo='Fecha' then 'date'
	end prueba,
	tipo, valor, id
	from  auxiliar au join especialidad e on e.nombre_esp=au.categoria
) as rs 
order by id_especialidad, id
;

insert into opc_preg (id_preg,resp_opc_preg)
select id_preg ,valor  from auxiliar join pregunta p using (pregunta) where valor is not null ;


drop table auxiliar ;



