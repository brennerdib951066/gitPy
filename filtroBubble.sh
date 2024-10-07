#!/usr/bin/env bash


arquivoLogin="/usr/bin/dibScripts/shells/stable/bibliotecas/credenciais/credencial.sh"
arquivoCor="/usr/bin/dibScripts/shells/stable/bibliotecas/cor/cores.txt"
arquivoNotificacao="/usr/bin/dibScripts/shells/stable/bibliotecas/notificacao/notificarWhatsApp.txt"
arquivoNotificacaoTelegram="/usr/bin/dibScripts/shells/stable/bibliotecas/notificacao/telegram.txt"
dataAtual="$(date +%Y-%m-%d)"
diaDaSemana=$(date +%A)
dataAtualMaisUm="$(date -d '1 days' +%Y-%m-%d)"
headerText='menu get bubble tipo de cliente'
listaPerguntas=('Thales Ramalho' 'Lais Morais' 'Nathália Santos' 'Calebe Pascoal/César/DF' 'Jully Isabelle/Pos Vendas')
listaPerguntasReceber=('receber aqui no konsole' 'receber no whatsapp')
interativo='no'

# INICIO DAS FUNÇÕES
receberNoKonsole(){
    echo -e "\E[42;1mNa data atual ${requisicao^^} vendeu\E[m \E[41;1m$((1+${count#*:}))\E[m"
}

enviarPeloServidor(){
        dataBrasil=$(awk -F- '{print $3"-"$2"-"$1}' <<<$dataAtual)
   { echo "Chamando o servidor para enviar a notificação"; sleep 2s ; }
    notificar "${idsBot[0]}" "AQUI ESTÁ O RELETÓRIO DE HOJE: (${diaDaSemana^^},${dataBrasil})"
    notificar "${idsBot[1]}" "AQUI ESTÁ O RELETÓRIO DE HOJE: (${diaDaSemana^^},${datBrasil})"
    for i in "${!listaPerguntas[@]}"; do
        sleep 2s
        echo "${listaPerguntas[i]}"
        count=$(curl -G -H "Authorization: Bearer 5b2a5efbc5fda2ffff948979031ac33a" --data-urlencode 'constraints=[{"key":"gerente","constraint_type":"equals","value": "'"${listaPerguntas[i]}"'"},{"key":"Created Date","constraint_type":"greater than","value":"'"${dataAtual}"'T00:00:00Z"},{"key":"Created Date","constraint_type":"less than","value":"'"${dataAtualMaisUm}"'T00:00:00Z"}]' 'https://www.sistemaviverbemseguros.com/api/1.1/obj/bc_outrosDados' 2>- | awk -F':' 'gsub(/[ ",]/,"",$0)&& /count/ {print}')

        if [[ "${resposta}" =~ [aA]pi ]]; then # aqui estou verificando o possivel erro de chave API
                    source "${arquivoNotificacaoTelegram}"
                    notificarTelegram "1017355630" "OPAH ERRO DE API DE UMA OLHADA LÁ"
                    exit
        fi

        for ((id=0;id<=1;id++)); do
            notificar "${idsBot[id]}" "${listaPerguntas[i]}, vendeu: $((${count#*:}+1))"
        done
    done
}
###############################################################
read -t 10 -p "você está no modo interativo ${interativo^^},Deseja mudar [S/n]" mudancaInterativo
[[ "${mudancaInterativo}" =~ (sim|SIM|s|S) ]] && interativo='yes'
if [[ "${interativo}" = 'yes' ]]; then
    if [[ -z $1 ]]; then
        echo $'\E[37;1mOnde deseja receber o total de vendas dos gerentes:\E[m'
        PS3=$'\E[37;1mOPÇÃO:\E[m   '
        select menu in "${listaPerguntasReceber[@]^^}"; do
            case $REPLY in
                1) { echo -e "Escolheu receber em ${REPLY^}"; receber="${listaPerguntasReceber[0]}"; break  ; }
                ;;
                2) { echo -e "Escolheu receber em ${REPLY^^}"; receber="${listaPerguntasReceber[1]}"; break ; }
            esac

        done
    else
            case $1 in
                1) { echo -e "Escolheu receber em ${REPLY^}"; receber="${listaPerguntasReceber[0]}" ; }
                ;;
                2) { echo -e "Escolheu receber em ${REPLY^^}"; receber="${listaPerguntasReceber[1]}"; }
            esac
    fi

    PS3=$'\E[36;1mOpção:\E[m   '
    echo "${headerText^^}"
    select menu in "${listaPerguntas[@]^^}"; do
        case $REPLY in
            1) { echo -e "\E[33;1mVoce escolheu ${REPLY} ${listaPerguntas[0]^}\E[m";  requisicao="${listaPerguntas[0]^}"  ; break ;}
            ;;
            2) { echo -e "\E[33;1m Voce escolheu ${REPLY} ${listaPerguntas[1]^}\E[m"; requisicao="${listaPerguntas[1]}"   ; break ;}
            ;;
            3) { echo -e "\E[33;1m Voce escolheu ${REPLY} ${listaPerguntas[2]^}\E[m"; requisicao="${listaPerguntas[2]}"   ; break ;}
            ;;
            4) { echo -e "\E[33;1m Voce escolheu ${REPLY} ${listaPerguntas[3]^}\E[m"; requisicao="${listaPerguntas[3]}"   ; break ;}
            ;;
            *) echo -e 'Escolha uma opção válida'
        esac
    done

    count=$(curl -G -H "Authorization: Bearer 5b2a5efbc5fda2ffff948979031ac33a" --data-urlencode 'constraints=[{"key":"gerente","constraint_type":"equals","value": "'"${requisicao}"'"},{"key":"Created Date","constraint_type":"greater than","value":"'"${dataAtual}"'T00:00:00Z"},{"key":"Created Date","constraint_type":"less than","value":"'"${dataAtualMaisUm}"'T00:00:00Z"}]' 'https://www.sistemaviverbemseguros.com/api/1.1/obj/bc_outrosDados' 2>- | awk -F':' 'gsub(/[ ",]/,"",$0)&& /count/ {print}')

    if [[ "${receber}" == "${listaPerguntasReceber[0]}" ]]; then
        receberNoKonsole
    else
        source "${arquivoNotificacao}"
        notificar "${idsBot[1]}" "Na data atual ${requisicao^^} vendeu $((1+${count#*:}))"
    fi
else
    sleep 5s
    source "${arquivoNotificacao}"
    enviarPeloServidor
fi
