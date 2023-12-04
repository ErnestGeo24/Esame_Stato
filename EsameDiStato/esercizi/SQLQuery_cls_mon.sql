select nome,monete_raccolte from Avasiloae.studente
inner join Avasiloae.monete 
on studente.id = monete.idstu
inner join Avasiloae.appartiene
on studente.id = appartiene.idstu
inner join Avasiloae.Classi_virtuali
on appartiene.idcv = Classi_virtuali.id
where idv = 12 and idcv = 15
order by monete_raccolte desc