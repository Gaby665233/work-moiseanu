lorem = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Deleniti cum dolorum maxime eos, quidem nihil sed id assumenda. Ex natus beatae quam inventore suscipit obcaecati numquam, voluptas iste distinctio eos, labore aperiam quod animi, nulla id accusantium velit illum ducimus? Sed ipsa molestias recusandae ut atque unde odit ipsum excepturi cupiditate nam quod saepe, iusto eveniet, commodi iste voluptatum asperiores enim! Sequi nobis sunt ipsa, ipsam tenetur explicabo adipisci doloremque autem quas dolorem, cumque nesciunt repudiandae dicta id delectus, officia labore? Adipisci exercitationem cumque facere nulla cupiditate saepe ad alias omnis itaque, reiciendis optio velit voluptatem hic amet dolores eveniet nam fugiat? Pariatur quia asperiores, facere laboriosam alias dolore iure illum repudiandae nihil modi nam reiciendis blanditiis veritatis deleniti necessitatibus ducimus iste ullam odit perspiciatis in obcaecati, sint numquam minima expedita? Omnis enim labore porro cum culpa consequuntur nihil asperiores doloremque quam recusandae cumque impedit consequatur temporibus tenetur suscipit fugiat deserunt beatae dolorum, iure assumenda voluptatibus. Reiciendis explicabo reprehenderit laudantium est nisi non id quibusdam quae eius suscipit iure unde laborum ratione delectus, at temporibus iste? Dolores quaerat laudantium, est temporibus saepe sunt ducimus inventore porro odit nihil non quo, voluptas beatae delectus magni officia, provident fugit iusto eos voluptatem omnis eius dignissimos. Voluptatem, iure odio sit nisi, cumque doloremque possimus dolorum quia ipsa, quod cum dolores. Pariatur similique at, nihil totam obcaecati sapiente suscipit, tempora animi ullam beatae, magnam ipsam alias ab sint aliquam deserunt excepturi cupiditate iure fugiat? Rerum quis vel culpa distinctio expedita nam. Necessitatibus quam maxime ratione neque temporibus doloremque dolores tempore eveniet, nulla, hic consequatur labore molestias esse aut magnam explicabo minima veniam dolor odio tenetur incidunt id! Ratione impedit possimus sapiente culpa similique. Officia impedit iusto voluptates aperiam aspernatur facilis consequuntur aliquam magnam commodi exercitationem nobis nemo, doloribus ea esse possimus officiis laborum quidem."
" ".join(lorem.split()[:20])
print(" ".join(lorem.split()[:20]))


text = "Ana are mere, pere și prune delicioase"
cuvinte_lista = text.split()  # împărțim textul în cuvinte
primele_5 = cuvinte_lista[:5] # luăm primele 5 cuvinte
cuvinte_rezultat = " ".join(primele_5)
print(cuvinte_rezultat)



lista = [123, 321, 123, 5, 31, 32, 35, 56, 50]
odd = []
even = []
i = 4
rezultat=[]
for x in lista:
    if x % 2:  
        odd.append(x)
    else:
        even.append(x)
    rezultat.append(x + i)



print("odd:", odd)
print("even:", even)
print("rezultat:", rezultat)
