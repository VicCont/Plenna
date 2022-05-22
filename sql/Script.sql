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
 returns TABLE (especialidades int) 
 as
$$
begin
	return query
	select id_especialidad  from permisos p 
	where p.id_doctor =id_d 
	and p.id_pac =id_pac 
	and p.activo ;
END;
 $$
LANGUAGE plpgsql;

CREATE or replace function   del_permiso (id_d int, id_p int,id_es int )
 returns void 
 as
$$
begin
update permisos  set activo =false where id_doctor =id_d and id_pac =id_p and id_especialidad =id_es ;
END;
 $$
LANGUAGE plpgsql;

CREATE or replace function   set_permiso (id_d int, id_p int,id_es int )
 returns void 
 as
$$
begin
insert into permisos (id_doctor,id_pac,id_especialidad) values
(id_d,id_p,id_es);
END;
 $$
LANGUAGE plpgsql;


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


select login('doctor 2','basura');

select login_admin ('doctor 2','basura');

drop function obtener_datos ;
CREATE or replace function   obtener_datos (id int )
 returns TABLE (id_preg int, id_especialidad int, respondidad int, pregunta varchar, resp_preg varchar, tipo tipos_input) 
 as
$$
begin
	return query
select p.id_preg ,p.id_especialidad , case when ra.resp_preg is not null then 1 else 0 end respondida,p.pregunta,ra.resp_preg,p.tipo  
from resp_abierta ra join preg_pac pp on (pp.id_pac=id and pp.id_preg_pac =ra.id_preg_pac) right join pregunta p using (id_preg) 
where p.tipo <'select'
union all
select op.id_preg,p.id_especialidad , case when pp.id_pac  is not null then 1 else 0 end respondida,p.pregunta,op.id_opc_preg ||','||op.resp_opc_preg , p.tipo 
from res_preg_opc rpo join preg_pac pp on (rpo.id_preg_pac=pp.id_preg_pac and pp.id_pac=id) right join opc_preg op using (id_opc_preg)
join pregunta p on (op.id_preg =p.id_preg)
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
	
end;
$$ language plpgsql ;

delete from resp_abierta 

select * from pregunta p where tipo='select';

select inserta_preg_pac_abierta (1,array [6,8,9,10,12,17,18,20,22,24,28,30],array ['hola','adios','meperdonas','bimbo','owo','prueba','respuesta 3','respuesta 7'])

select * from (select * from unnest([14,16,19,25,27]) with ordinality 

select * from inserta_preg_pac  (1, ARRAY [11,2,5,1,3,2]);

insert into resp_abierta (id_preg_pac,resp_preg)
select foranea,aux.valor from inserta_preg_pac (1,ARRAY [1,2,2,2,5,1,3,2]) as inicial join (select * from unnest (ARRAY [1,2,2,2,5,1,3,2]) with ordinality as preguntas(valor, llave)) as preguntas
on inicial.pregunta =preguntas.valor 
join (select * from  unnest (array['hola','adios','meperdonas','bimbo','owo','prueba']) with ordinality as respuestas(valor, llave)) as aux using (llave)
returning *
;


select * from pregunta p where tipo<'radio';

create type respuesta_pregunta_cerrada as (
id_corr int,
id_resp int
);

