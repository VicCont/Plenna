select p.id_preg ,pp.id_pac , case when ra.resp_preg is not null then 1 else 0 end ,p.pregunta,ra.resp_preg   
from pregunta p right join preg_pac pp on (p.id_preg= pp.id_preg  )
right join resp_abierta ra using (id_preg_pac);

select p.id_preg ,p.id_especialidad , case when ra.resp_preg is not null then 1 else 0 end respondida,p.pregunta,ra.resp_preg,p.tipo  
from resp_abierta ra join preg_pac pp on (pp.id_pac=1 and pp.id_preg_pac =ra.id_preg_pac) right join pregunta p using (id_preg) 
where p.tipo <'select'
union all
select op.id_preg,p.id_especialidad , case when pp.id_pac  is not null then 1 else 0 end respondida,p.pregunta,op.id_opc_preg ||','||op.resp_opc_preg , p.tipo 
from res_preg_opc rpo join preg_pac pp on (rpo.id_preg_pac=pp.id_preg_pac and pp.id_pac=1) right join opc_preg op using (id_opc_preg)
join pregunta p on (op.id_preg =p.id_preg)
order by 1;

insert into permisos (id_doctor,id_pac,id_especialidad)
(1,2,3);

select id_especialidad  from permisos p 
where p.id_doctor =1 
and p.id_pac =1
and p.activo ;

do $$
declare id_doc int;
begin
   -- select the number of films from the actor table
	select login('doctor 1','basura') into id_doc ;
	select * from doctor d where d.id_doctor =id_doc and d."admin" into id_doc  ;

   -- show the number of films
   raise notice 'id del doc: %', id_doc ;
end; $$;


SELECT [3,3,4,56];




select * from doctor d 
where d.usuario ='doctor 1'
and d.hash_pass ='basura'
and activo 

insert into permisos (id_doctor,id_pac,id_especialidad)
values 
(1,1,1),
(1,1,4),
(2,1,1),
(2,1,5)


insert into doctor (nom_doc,usuario,hash_pass,"admin",id_especialidad)
values 
('doctor 1','doctor 1','basura',false,1),
('doctor 2','doctor 2','basura',true,1)

select *,p.tipo from pregunta p ;



--insert into preg_pac  (id_preg, id_pac)
--select distinct id_preg, 1 from opc_preg op ;
--insert into res_preg_opc (id_preg_pac,id_opc_preg)
--select id_preg_pac , id_opc_preg from (select distinct on (id_preg) op.id_preg ,pp.id_preg_pac , id_opc_preg  from opc_preg op join preg_pac pp on (pp.id_preg =op.id_preg  and pp.id_pac =1)) as aux;