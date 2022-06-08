create type respuesta_pregunta_abierta as (
id_corr int,
respuesta text
);


select * from paciente p ;

drop function prueba  ;

CREATE or replace function   inserta_preg_pac (id int, lista int[] )
 returns TABLE (foranea int, pregunta int) 
 as
$$
begin
	return query
	insert into preg_pac (id_pac,id_preg)
	select id, y.valores from (select distinct (valores) from unnest(lista) as aux(valores) order by valores) as y 
 	returning id_preg_pac ,id_preg  ;
END;
 $$
LANGUAGE plpgsql;



CREATE or replace function   get_permisos (id_d int, id_p int )
 returns TABLE (especialidades int, nom_esp varchar) 
 as
$$
begin
	return query
	select id_especialidad, nombre_esp  from permisos p join especialidad using (id_especialidad)
	where p.id_doctor =id_d 
	and p.id_pac =id_p
	and p.activo ;
END;
 $$
LANGUAGE plpgsql;


	select id_especialidad, e.nombre_esp  from permisos p join especialidad e using (id_especialidad)
	where p.id_doctor =1 
	and p.id_pac =2
	and p.activo ;


CREATE or replace function   is_authorized (doc int, pac int )
 returns boolean
 as
$$
declare
   retorno boolean ; 
begin
		select case when count(*)=0 then false else true end from permisos p where id_doctor =doc and id_pac =pac and activo 
		into retorno ;
	return retorno  ;
END;
 $$
LANGUAGE plpgsql;

select is_authorized(1,1);

CREATE or replace function   login (usu varchar, hash varchar )
 returns int
 as
$$
declare
   id_doc integer; 
begin
		select id_doctor from doctor d 
		where d.usuario =usu
		and d.hash_pass =hash
		and activo into id_doc;
	return id_doc ;
END;
 $$
LANGUAGE plpgsql;

CREATE or replace function   login_admin (usu varchar, hash varchar )
 returns int
 as
$$
declare id_doc int;
begin
	select login(usu,hash) into id_doc ;
	select * from doctor d where d.id_doctor =id_doc and d."admin" into id_doc  ;

   return id_doc  ;
END;
 $$
LANGUAGE plpgsql;

CREATE or replace function obtener_insights (id int )
 returns table (nom_doc varchar, nom_pac varchar, comentario varchar)
 as
$$
begin
	return query
	select d.nom_doc ,p.nombre ,i.comentario  from insight i join paciente p using (id_pac)
	join doctor d using (id_doctor) where id_pac =id ;
END;
 $$
LANGUAGE plpgsql;

CREATE or replace function get_docs ( )
 returns table (id_doc int, nombre varchar, nom_especialidad varchar)
 as
$$
begin
	return query
	select id_doctor,nom_doc,e.nombre_esp  from doctor d join especialidad e using (id_especialidad) where activo ;
END;
 $$
LANGUAGE plpgsql;

select * from get_docs();

CREATE or replace function get_permisos_doc (id int)
 returns table (id_doc int, nombre varchar, nom_especialidad varchar)
 as
$$
begin
	return query
select p2.id_pac, p2.nombre , nombre_esp  from permisos p join especialidad e using (id_especialidad) join paciente p2 using (id_pac) where id_doctor=id and activo ;
END;
 $$
LANGUAGE plpgsql;



select p2.id_pac, p2.nombre , nombre_esp  from permisos p join especialidad e using (id_especialidad) join paciente p2 using (id_pac) where id_doctor=1 and activo ;

select id_doctor,nom_doc,e.nombre_esp  from doctor d join especialidad e using (id_especialidad) where activo order by e.id_especialidad ;

select d.nom_doc ,p.nombre ,i.comentario  from insight i join paciente p using (id_pac)
join doctor d using (id_doctor) where id_pac =2 ;

CREATE or replace function insertar_insight (doc int, pac int, coment varchar )
 returns boolean
 as
$$
declare authorized boolean;
begin
	select is_authorized(doc,pac) into authorized;
	if authorized  then
	     insert into insight (id_doctor,id_pac,comentario)
	     values (doc,pac,coment);
	  end if;
	 return authorized ;
END;
 $$
LANGUAGE plpgsql;

select * from permisos p ;

select is_authorized (1,2);
select insertar_insight (1,2,'ya no tiene perro bonito');


select login('doctor 2','basura');

select login_admin ('doctor 2','basura');


CREATE or replace function obtener_pacientes_doc (id int )
 returns table (id_pac int, nombre varchar, clave_pac  varchar)
 as
$$
begin
	return query
	select distinct on (p.id_pac)  p.id_pac , p2.nombre,p2.clave_pac  from permisos p join paciente p2 on (p2.id_pac=p.id_pac and  id_doctor=id) where p.activo ;
END;
 $$
LANGUAGE plpgsql;

select * from obtener_pacientes_doc(1);

select * from obtener_datos (8);

drop function obtener_datos ;
CREATE or replace function   obtener_datos (id int )
 returns TABLE (id_preg int, id_especialidad int, respondidad int, pregunta varchar, resp_preg varchar, tipo tipos_input,nom_espe varchar) 
 as
$$
begin
	return query
select p.id_preg ,p.id_especialidad , case when ra.resp_preg is not null then 1 else 0 end respondida,p.pregunta,ra.resp_preg,p.tipo, esp.nombre_esp  
from resp_abierta ra join preg_pac pp on (pp.id_pac=id and pp.id_preg_pac =ra.id_preg_pac) right join pregunta p using (id_preg) 
join especialidad esp on esp.id_especialidad =p.id_especialidad 
where p.tipo <'select'
union all
select op.id_preg,p.id_especialidad , case when pp.id_pac  is not null then 1 else 0 end respondida,p.pregunta,op.id_opc_preg ||','||op.resp_opc_preg , p.tipo ,esp.nombre_esp  
from res_preg_opc rpo join preg_pac pp on (rpo.id_preg_pac=pp.id_preg_pac and pp.id_pac=id) right join opc_preg op using (id_opc_preg)
join pregunta p on (op.id_preg =p.id_preg) join especialidad esp on esp.id_especialidad =p.id_especialidad 
order by 1;
END;
 $$
LANGUAGE plpgsql;

select * from obtener_datos (1);

CREATE or replace function   inserta_preg_pac_abierta (id int, lista_preg int[],lista_resp varchar[] )
returns void
as $$ 
begin 
insert into resp_abierta (id_preg_pac,resp_preg)
select foranea,aux.valor from inserta_preg_pac (id,lista_preg) as inicial join (select * from unnest (lista_preg) with ordinality as preguntas(valor, llave)) as preguntas
on inicial.pregunta =preguntas.valor 
join (select * from  unnest (lista_resp) with ordinality as respuestas(valor, llave)) as aux using (llave);
end;
$$ language plpgsql ;


create or replace function  inserta_resp_cerrada(id int, lista_preg int[], list_ids_resp int [])
returns void 
as $$
begin 
insert into res_preg_opc  (id_preg_pac,id_opc_preg)
select foranea,aux.valor from inserta_preg_pac (id,lista_preg) as inicial join (select * from unnest (lista_preg) with ordinality as preguntas(valor, llave)) as preguntas
on inicial.pregunta =preguntas.valor 
join (select * from  unnest (list_ids_resp) with ordinality as respuestas(valor, llave)) as aux using (llave);
end;
$$ language plpgsql ;

create or replace function  actualiza_resp_abierta(id int, lista_preg int[], list_ids_resp varchar [],  id_esp int)
returns void 
as $$
begin 
create temp table if not exists ids_borrado as select id_preg_pac  from preg_pac pp join pregunta p using (id_preg ) where p.id_especialidad=id_esp and id_pac=id;
delete from res_preg_opc rpo where id_preg_pac in (select * from ids_borrado);
delete from resp_abierta where id_preg_pac in (select * from ids_borrado);
delete from preg_pac where id_preg_pac  in (select * from ids_borrado);
drop table ids_borrado ;
perform inserta_preg_pac_abierta(id,lista_preg,list_ids_resp);
end;
$$ language plpgsql ;


select actualiza_resp_abierta  (8,array [31, 32, 33, 37, 38],array ['armanda', '34', 'estudiante', 'True', '333'], 13)

select inserta_preg_pac_abierta (1,array [6,8,9,10,12,17,18,20,22,24,28,30],array ['hola','adios','meperdonas','bimbo','owo','prueba','respuesta 3','respuesta 7'])

select * from (select * from unnest([14,16,19,25,27]) with ordinality 

select * from inserta_preg_pac  (1, ARRAY [11,2,5,1,3,2]);

insert into resp_abierta (id_preg_pac,resp_preg)
select foranea,aux.valor from inserta_preg_pac (9,ARRAY [34,35,36]) as inicial join (select * from unnest (ARRAY [34,35,36]) with ordinality as preguntas(valor, llave)) as preguntas
on inicial.pregunta =preguntas.valor 
join (select * from  unnest (array[54,59,62]) with ordinality as respuestas(valor, llave)) as aux using (llave)
returning *
;


select * from pregunta p where tipo<'radio';

create type respuesta_pregunta_cerrada as (
id_corr int,
id_resp int
);

CREATE or replace function remueve_permisos (id_doct int, id_paciente int,lista_perm int[] )
returns void
as $$ 
begin 
update permisos set activo =false where id_doctor =id_doct  and id_pac =id_paciente  and id_especialidad = any (lista_perm);
end;
$$ language plpgsql ;

select * from permisos p join especialidad e using (id_especialidad) ;

CREATE or replace function get_permisos_faltantes (id_doct int, id_paciente int )
returns TABLE (id_espc int, nombre varchar)
as $$ 
begin
return query 
select e.id_especialidad,e.nombre_esp  from especialidad e 
left join permisos p ON (id_pac=id_paciente  and id_doctor =id_doct  and p.id_especialidad=e.id_especialidad) where id_permiso is null or not p.activo ;
end;
$$ language plpgsql ;

select * from get_permisos_faltantes (1,1);

drop function get_preguntas_esp ;
CREATE or replace function get_preguntas_esp (id_esp int )
returns TABLE (id_espc int, tipo tipos_input  )
as $$ 
begin
return query 
select id_preg,p.tipo  from pregunta p where p.id_especialidad =id_esp  ;
end;
$$ language plpgsql ;

select * from get_preguntas_esp (13);



CREATE or replace function insert_permisos (id_doct int, id_paciente int , lista int[])
returns void
as $$ 
begin
update permisos set activo =true  where id_doctor =id_doct  and id_pac =id_paciente  and id_especialidad = any(lista);

insert into permisos (id_doctor, id_pac,id_especialidad)
select id_doct ,id_paciente  ,e.id_especialidad  from especialidad e left join permisos p ON (id_pac=id_paciente  and id_doctor =id_doct  and p.id_especialidad=e.id_especialidad)
where id_permiso is null and e.id_especialidad = any(lista);

end;
$$ language plpgsql ;

delete from permisos ;

select insert_permisos (1,2,array[1,2,3,4,5,6])

select e.id_especialidad,e.nombre_esp  from especialidad e left join permisos p ON (id_pac=3 and id_doctor =1 and p.id_especialidad=e.id_especialidad) where id_permiso is null or not p.activo ;


