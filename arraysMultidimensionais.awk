#!/usr/bin/env -S awk -f

BEGIN{

    # Definir como o awk irá tratar a ordem da iteração
    PROCINFO["sorted_in"]="@ind_str_asc"

    alunos["João"]["bim1"] = 8
    alunos["João"]["bim2"] = 8
    alunos["João"]["bim3"] = 9
    alunos["João"]["bim4"] = 7.8

    alunos["Maria"]["bim1"] = 6
    alunos["Maria"]["bim2"] = 5
    alunos["Maria"]["bim3"] = 6.8
    alunos["Maria"]["bim4"] = 7.9

    # Não esquecer que a variavel do loop(elemento) so recebe o index da array
    for (elemento in alunos){
        print alunos[elemento]["bim4"]
    }

    # notas do joao
    print "\n"
    for (elemento in alunos["João"]){
        print elemento, ":", alunos["João"][elemento]
    }

    # Buscando todas as notas dos alunos
    print "\n"
    for(aluno in alunos) {
        print aluno
        for(nota in alunos[aluno]){
            bimestre = nota
            print "A nota do aluno(a)",aluno,"no",bimestre,"é de: ",alunos[aluno][nota]
            if(aluno == "João"){
                notaTotalJoao += alunos[aluno][nota]
            }
            else{
                notaTotalMaria += alunos[aluno][nota]
            }

        }
    }
    print
    print "A nota total de joão é:",notaTotalJoao,"media = ",notaTotalJoao/4
    print "A nota total de maria é:",notaTotalMaria,"media = ",notaTotalMaria/4
}


