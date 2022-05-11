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



CREATE or replace function   inserta_preg_pac_abierta (id int, lista_preg int[],lista_resp varchar[] )
returns void
as $$ 
begin 
insert into resp_abierta (id_preg_pac,resp_preg)
select foranea,aux.valor from inserta_preg_pac (1,lista_preg) as inicial join (select * from unnest (lista_preg) with ordinality as preguntas(valor, llave)) as preguntas
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

select * from pregunta p where tipo='select';


select * from (select * from unnest([14,16,19,25,27]) with ordinality 

select * from inserta_preg_pac  (1, ARRAY [11,2,5,1,3,2]);

insert into resp_abierta (id_preg_pac,resp_preg)
select foranea,aux.valor from inserta_preg_pac (1,ARRAY [1,2,2,2,5,1,3,2]) as inicial join (select * from unnest (ARRAY [1,2,2,2,5,1,3,2]) with ordinality as preguntas(valor, llave)) as preguntas
on inicial.pregunta =preguntas.valor 
join (select * from  unnest (array['hola','adios','meperdonas','bimbo','owo','prueba']) with ordinality as respuestas(valor, llave)) as aux using (llave)
returning *
;


create type respuesta_pregunta_cerrada as (
id_corr int,
id_resp int
);

