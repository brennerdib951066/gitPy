#!/usr/bin/env bash


arquivoLogin="/usr/bin/dibScripts/shells/stable/bibliotecas/credenciais/credencial.sh"
arquivoCor="/usr/bin/dibScripts/shells/stable/bibliotecas/cor/cores.txt"
arquivoNotificacao="/usr/bin/dibScripts/shells/stable/bibliotecas/notificacao/notificarWhatsApp.txt"

# Criando função para buscar a aréa de trabalho do usuário que vem como padrão no acoesDoSistema
diretorioUsuario()
{
    diretorioDeTrabalhoSistema=$(
    awk '
        BEGIN{
            FS="/"
        } $0 ~ /Área/{
            gsub(/"/,"",$0)
            print $2
        }
    ' ~/'.config/user-dirs.dirs'
    )
}
diretorioUsuario
# função de retirar os espaços das resposta do usuário que vem da variavel opcaoAtual
retirarEspacos()
{
    semEspacos="${1#* }"
    #echo -e "\E[31;1mPARAMETRO ${1}\E[m"

}
# função de abrir os arquivos
abrirArquivos()
{
    #echo "${1^^}"
    local escolherTipoArquivoLista=($'sair\n' $'python(.py)\n' $'awk(.awk)\n' $'shell(.sh)')
    local valorInput='arquivo'
    arquivoTipoEscolhido="$(fzf --prompt "${valorInput^^}:   "<<<${escolherTipoArquivoLista[@]^^})"
    retirarEspacos "${arquivoTipoEscolhido}"
    arquivoTipoEscolhido="$semEspacos"
    echo $arquivoTipoEscolhido
    # verificando com o case o resulatado da resposta do usuário
    case "${arquivoTipoEscolhido}" in
        "SAIR"       ) { echo $'OKAI saindo fora'; exit 1 ; }
        ;;
        "PYTHON(.PY)") { echo "ESCOLHESTES PYTHONNNNN!!!"
                        arquivoPython=( $'sair\n'
                                        ~/''${diretorioDeTrabalhoSistema}'/py/'$'acoesDoSistema.py\n'
                                        ~/''${diretorioDeTrabalhoSistema}'/py/'$'cadastrarLeadsBotBotConversa.py\n'
                                        ~/''${diretorioDeTrabalhoSistema}'/py/'$'pegarLead.py\n' ~/''${diretorioDeTrabalhoSistema}'/py/'$'botConversaAbrir.py\n'
                                        ~/''${diretorioDeTrabalhoSistema}'/py/'$'FLET.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'acoesDoSistema.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'botConversaAbrir.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'cadastrarLeadsBotBotConversa.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'deslogarViver.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'logarViverBemSeguros.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'notificacaoTelegram.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'notificarBotConversa.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'notificarNtfy.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'paginasViverBem.py\n'
                                        '/usr/bin/dibScripts/python/bibliotecas/'$'pegarLead.py\n'
                                    )
                                    editores=('/usr/bin/vima' '/usr/bin/nano' '/usr/bin/xed' '/usr/bin/kate')
                                    editoresEncontrados=()  # Esperando o loop fazer a verificação para ver qual programa existe na maquina
                                    abrirArquivo=$(fzf --prompt "ARQUIVO:   " <<<${arquivoPython[@]})
                                    retirarEspacos "${abrirArquivo}"

                                    for ((i=0;i<${#editores[@]};i++)); do
                                           if ! type -P ${editores[i]} &>-;then
                                                    continue
                                           fi
                                            editoresEncontrados[i]="${editores[i]}"
                                            editores[i]=${editores[i]^^}
                                    done

                                    #echo -e "\E[31;1mencontrei esses editores: ${editoresEncontrados[@]##*/}\E[m"
                                    usarPrograma=$(fzf --prompt "ABRIR COM:   " <<<"$(printf "%s\n" ${editoresEncontrados[@]})")
                                    abrirArquivo=$semEspacos

                                    ${usarPrograma##*/} "${abrirArquivo}" # abrindo o arquivo com o programa escolhido


        }
        ;;
        "AWK(.AWK)"  ) { echo "ESCOLHESTES AWKZINHO!!!"    ;}
        ;;
        "SHELL(.SH)"  ) { echo "ESCOLHESTES SHELL!!!"      ;}
        ;;
        *) echo -e 'Opção inválida!'
    esac

}
abrirDocumentacoes()
{
    echo "${1^^}"
}

# função principal de menu inicial
menuInicial()
{
    local opcaoMenuLista=($'sair\n' $'abrir arquivos\n' $'documentações\n')
    local valorInput='opção'
    local opcaoAtual=$(fzf --prompt "${valorInput^^}:   "<<< "${opcaoMenuLista[@]^^}")

    retirarEspacos "${opcaoAtual}"
    opcaoAtual="$semEspacos"

    #echo "${opcaoAtual^^}"
    # Verificando com o case qual é resposta do usuário
    echo -e "\E[31;1mRESPOSTA ATUAL:${opcaoAtual}\E[m"
    case "${opcaoAtual}" in
        "sair"|"SAIR"                    ) exit # aqui devo chamar a função correspondente
        ;;
        "abrir arquivos"|"ABRIR ARQUIVOS") abrirArquivos "Sim cou abrir seus arquivos pode deixar" # aqui devo chamar a função correspondente
        ;;
        "documentações"|"DOCUMENTAÇÕES"  ) abrirDocumentacoes "sim vou abrir suas documentações certinho" # aqui devo chamar a função correspondente
        ;;
        *) echo -e $'\E[31;1mEssa resposta não é válida!\E[m'

    esac
}
menuInicial # Chamando a função de menu principal

