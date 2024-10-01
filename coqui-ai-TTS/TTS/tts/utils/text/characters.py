import logging
from dataclasses import replace
from typing import Dict

from TTS.tts.configs.shared_configs import CharactersConfig

logger = logging.getLogger(__name__)


def parse_symbols():
    return {
        "pad": _pad,
        "eos": _eos,
        "bos": _bos,
        "characters": _characters,
        "punctuations": _punctuations,
        "phonemes": _phonemes,
    }


# DEFAULT SET OF GRAPHEMES
_pad = "<PAD>"
_eos = "<EOS>"
_bos = "<BOS>"
_blank = "<BLNK>"  # TODO: check if we need this alongside with PAD
_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_punctuations = "!'(),-.:;? "

#addText = "-k-m-p-t-aŋoiãbeɛããaʔaiaiaĩãiɪaʊiaudzaĩdzaĩʑaiʑaiʑɪaʊʑɪaʊakamamapɕɪaʊɕɪaʊatauaubababãbãbaʔbɪaʊbɪaʊbaibaibaĩbaĩbakbambambapbatbaubaubɨbɨbebebẽbẽbɪəbɪəbobobɪɛnbɪɛnbibibĩbĩbimbimbinbinbiŋbiŋbitbiubiubiũbiũbɪkbɔbɔbɔ̃bɔ̃bɔkbɔŋbɔŋbuabuabuaibuaibuanbuanbububuebuedzaidzaidzaʔdzadzadzãdzãdzakdzamdzamdzapdzatdzaudzaudzedzedzẽdzẽdzodzodzŋ̍dzŋ̍dzɔdzɔdzɔ̃dzɔ̃dzɔkdzɔŋdzɔŋdzuaidzuaidzuadzuadzuandzuanʑueʑuedzudzueẽẽiəʔɪəiəʑioʑiuɪɛnianʑɪɛnʑɪɛnsɪɛnsɪɛnooɕioɕiogagagãgãgaʔgɪaʊgɪaʊgaigaigaĩgaĩgakgamgamgapgatgaugaugegegẽgẽgɪəgiugɪəʔgogogɪɛngɪɛngɨgɨgigigĩgĩgimgimgiŋgiŋgingingiugiugiũgiũgɪkgŋ̍gŋ̍gɔgɔgɔ̃gɔ̃gɪɔkgɔkgɪɔŋgɪɔŋgɔŋgɔŋguaguaguaiguaiguanguanguegueguguhahahãhãhaʔhɪaʊhɪaʊhaihaihaĩhaĩhakhamhamhaphathauhauhehehẽhẽhɪəʔhɪəhiuhohohɪɛnhɪɛnhɨhɨhihihĩhĩhimhimhiŋhiŋhinhinhiphithiuhiuhiũhiũhɪkhŋ̍hŋ̍hɔhɔhɔ̃hɔ̃hɪɔkhɔkhɪɔŋhɪɔŋhɔŋhɔŋhuahuahuaihuaihuanhuanhuehuehuhuɕiaiɕiaiɕiaĩɕiaĩʑiaʔʑiaʑiaʑiãʑiãʑiakɕiakʑiamʑiamɕiamɕiamʑiapɕiapɕiaʔɕiaɕiaɕiãɕiãʑiatɕiatʑieʑieʑiẽʑiẽɕieɕieɕiẽɕiẽiiĩĩɨɨsĩsĩɕiiũɕiiũʑid͡ʑimimʑimʑimsimsimiŋiŋʑiŋ̍ʑiŋ̍siŋsiŋininʑinʑinɕinɕinʑiɔʑiɔʑiɔ̃ʑiɔ̃ʑiɔkɕiɔɕiɔɕiɔ̃ɕiɔ̃ipʑipsiɕsɨsɨitʑitɕiuanɕiuanɕiuaɕiuaɕiueɕiueiuiuiũiũʑiuʑiuɕiuɕiuʑɨʑɨkaikaikaĩkaĩkʰaikʰaikʰaĩkʰaĩkaʔkakakãkãkʰaʔkʰakʰakʰãkʰãkʰɪaʊkʰɪaʊkɪaʊkɪaʊkakkʰakkamkamkʰamkʰamkapkʰapkatkʰatkaukaukʰaukʰaukekekẽkẽkʰekʰekʰẽkʰẽkʰɪəʔkʰɪəkʰiukʰokʰoikkɪəʔkɪəkiukokokʰɪɛnkʰɪɛnkɪɛnkɪɛnkʰikʰikʰĩkʰĩkikikĩkĩkʰimkʰimkimkimkiŋkiŋkʰiŋkʰiŋkʰinkʰinkinkinkʰipkipkʰitkitkʰiukʰiukʰiũkʰiũkiukiukiũkiũʑɪkkʰɨkʰɨkɨkɨkɪkkʰɪkkʰŋ̍kʰŋ̍kŋ̍kŋ̍kʰɔkʰɔkʰɔ̃kʰɔ̃kʰɪɔkkʰɔkkɪɔkkɔkkɔkɔkɔ̃kɔ̃kʰɪɔŋkʰɪɔŋkʰɔŋkʰɔŋkɪɔŋkɪɔŋkɔŋkɔŋsɪkkʰuaikʰuaikuaikuaikʰuakʰuakuakuakʰuankʰuankuankuankʰuekʰuekuekuekʰukʰukukulailailaĩlaĩlaklaʔlalalãlãlɪaʊlɪaʊlamlamlaplatlaulaulelelẽlẽlɪəʔlɪəliulololɪɛnlɪɛnlililĩlĩlimlimliŋliŋlinlinlipliuliuliũliũlɪklɨlɨlŋ̍lŋ̍lɪɔklɔklɔlɔlɔ̃lɔ̃lɪɔŋlɪɔŋlɔŋlɔŋluailuailualualuanluanlueluelulumaimaimaĩmaĩmakmaʔmamamãmãmɪɛnmɪɛnmammammapmatmaumaumememẽmẽmomomimimĩmĩmiŋmiŋmiũmiũmɪkmɨmɨm̩m̩m̩mŋ̍mŋ̍mɔkmɔmɔmɔ̃mɔ̃mɔŋmɔŋmuaimuaimuamuamuanmuanmuemuemumunainainaĩnaĩnaknamnamnaʔnananãnãnɪɛnnɪɛnnapnatnaunaunenenẽnẽnonoŋ̍ŋ̍niŋniŋnininĩnĩniũniũnɪknŋ̍nŋ̍nɨnɨnɔknɔŋnɔŋnɔnɔnɔ̃nɔ̃nuainuainuannuannuanuanuenuenunuiɔkɔkɔmɔmɪɔŋiɔŋʑɪɔŋʑɪɔŋɔŋɔŋɕɪɔŋɕɪɔŋɔɔɔ̃ɔ̃paipaipaĩpaĩpʰaipʰaipʰaĩpʰaĩpakpʰakpampampʰampʰampaʔpapapãpãpʰaʔpʰapʰapʰãpʰãpʰɪaʊpʰɪaʊpɪaʊpɪaʊpappʰappatpʰatpaupaupʰaupʰaupʰɪɛnpʰɪɛnpɪɛnpɪɛnpepepẽpẽpʰepʰepʰẽpʰẽpʰɪəpʰɪəpʰopʰopɪəpiupopopʰimpʰimpimpimpiŋpiŋpʰiŋpʰiŋpʰinpʰinpinpinpʰiphipʰĩpʰĩpipipĩpĩpʰitpitpʰiũpʰiũpiupiupiũpiũpɪkpʰɪkpʰŋ̍pʰŋ̍pŋ̍pŋ̍pʰɔkpɔkpʰɔŋpʰɔŋpɔŋpɔŋpʰɔpʰɔpʰɔ̃pʰɔ̃pɔpɔpɔ̃pɔ̃pʰɨpʰɨpɨpɨpʰuaipʰuaipuaipuaipʰuanpʰuanpuanpuanpʰuapʰuapuapuapʰuepʰuepuepuepʰupʰupupusaisaisaĩsaĩsaksamsamsapsaʔsasasãsãsatsausausesesẽsẽsɪəʔsososipsitsiũsiũsŋ̍sŋ̍sɪɔksɔksɔmsɔmsɔŋsɔŋsɔsɔsɔ̃sɔ̃ɕuaiɕuaisuansuansuasuasuesuesusutɕʰɪaʊtɕʰɪaʊtsɪaʊtsɪaʊtsaitsaitɕaĩtɕaĩtaitaitaĩtaĩtʰaitʰaitʰaĩtʰaĩtaktʰaktamtamtʰamtʰamtaptʰaptaʔtatatãtãtʰaʔtʰatʰatʰãtʰãtʰɪaʊtʰɪaʊtɪaʊtɪaʊtattʰattautautʰautʰautsɨtsɨtɕʰiotɕʰiutɕʰɪəʔtɕɪəʔtsʰɪɛntsʰɪɛntsɪɛntsɪɛntʰɪɛntʰɪɛntɪɛntɪɛntetetẽtẽtʰetʰetʰẽtʰẽtʰɪətʰiutʰotʰotɪəʔtɪətiutototɕʰiatɕʰiatɕʰiãtɕʰiãtɕʰiaʔtɕiaʔtɕiatɕiatɕiãtɕiãtɕʰiaitɕʰiaitɕʰiaĩtɕʰiaĩtɕʰiaktɕiaktɕʰiamtɕʰiamtɕiamtɕiamtɕʰiaptɕiaptɕʰiattɕiattsʰit͡ɕʰtsʰɨtsʰɨtsit͡ɕtsĩtsĩtɕʰietɕʰietɕʰiẽtɕʰiẽtɕietɕietɕiẽtɕiẽtsɪətsiutsʰĩtsʰĩtɕʰiiũtɕʰiiũtsʰimtsʰimtsimtsimtʰimtʰimtimtimtɕʰintɕʰintsʰiŋtsʰiŋtsiŋtsiŋtiŋtiŋtʰiŋtʰiŋtʰintʰintintintɕʰiɔtɕʰiɔtɕʰiɔ̃tɕʰiɔ̃tɕiɔtɕiɔtɕiɔ̃tɕiɔ̃tɕʰiɔktɕiɔktɕʰiptɕiptɕʰittɕittʰithitʰĩtʰĩtititĩtĩtittɕʰiuatɕʰiuatɕʰiuaitɕʰiuaitɕʰiuantɕʰiuantɕʰiutɕʰiutsiutsiutɕiũtɕiũtɕʰiuetɕʰiuetʰiutʰiutʰiũtʰiũtiutiutiũtiũtsʰɪktsɪktɪktʰɪktʰŋ̍tʰŋ̍tŋ̍tŋ̍tʰɪɔktʰɔktɪɔktɔktɔmtɔmtɕʰɪɔŋtɕʰɪɔŋtɕɪɔŋtɕɪɔŋtʰɪɔŋtʰɪɔŋtʰɔŋtʰɔŋtɪɔŋtɪɔŋtɔŋtɔŋtʰɔtʰɔtʰɔ̃tʰɔ̃tɔtɔtɔ̃tɔ̃tsaʔtsatsatsãtsãtsʰatsʰatsʰãtsʰãtsʰaʔtsaĩtsaĩtsʰaitsʰaitsʰaĩtsʰaĩtsaktsʰaktsamtsamtsʰamtsʰamtsaptsʰaptsattsʰattsautsautsʰautsʰautsetsetsẽtsẽtsʰetsʰetsʰẽtsʰẽtsʰotsʰotsotsotsintsintsʰiũtsʰiũtsiũtsiũtsʰŋ̍tsʰŋ̍tsŋ̍tsŋ̍tsʰɔtsʰɔtsʰɔ̃tsʰɔ̃tsɔtsɔtsɔ̃tsɔ̃tsʰɔktsɔktsʰɔŋtsʰɔŋtsɔŋtsɔŋtsʰuatsʰuatɕuatɕuatsʰuaitsʰuaitɕuaitɕuaitsʰuantsʰuantɕuantɕuantsʰutsʰutsutsutsʰuetsʰuetɕuetɕuetʰɨtʰɨtɨtɨtʰuaitʰuaituaituaitʰuantʰuantuantuantʰuatʰuatuatuatʰuetʰuetuetuetʰutʰututuuaiuaiuanuanuauaueueuuuãiuãueʔuʔŋʔɔʔɔpiuʔĩʔiauʔiãuiʔãʔauʔeʔẽʔiaʔaŋiaiakiamiaŋiãʔhjikhingi-ʔ-k-mnəŋ-p-tanaŋãũəgiaŋiapiatiãudzkkʰlmʔnəʔəppʰsttʰt͡st͡sʰuaʔuatuiunũut"
addText = "-k-m-p-t-ʔaiamanap̚at̚auaĩaŋbbabaibambapbaubaĩbebeʔbibik̚bimbinbit̚biubiŋbiũbiɑnbiɑt̚biɑubiəbiʔbobubuabuaibuanbuebueʔbuibuiʔbunbut̚buɑbuɑnbuɑt̚buɑɪʔbuɑʔbuʔbãbĩbɑbɑk̚bɑnbɑt̚bɑubɑŋbɑɪbɑʔbɑ̃ubɔbɔk̚bɔnbɔŋbɔ̃bɔ̃ʔbəbɨbɪaʊbɪəbɪɛnbẽdzdzadzaidzakdzamdzapdzatdzaudzaĩdzaʔdzedzodzudzuadzuaidzuandzãdzŋ̍dzɔdzɔkdzɔŋdzɔ̃dzẽeeŋeʔggagaigamgapgatgaugaĩgaʔgegeʔgigik̚gimgingiugiŋgiũgiũʔgiɑgiɑmgiɑngiɑp̚giɑt̚giɑugiɑuʔgiɑŋgiɑʔgiɔk̚giɔŋgiɔŋʔgiəgiəʔgoguguaguaiguanguegueʔguiguiʔgunguɑguɑnguɑt̚guɑŋguɑɪguɑ̃ɪgãgĩgŋ̍gũigũʔgɑgɑk̚gɑmgɑngɑugɑuʔgɑŋgɑɪgɑ̃ugɔgɔk̚gɔngɔŋgɔ̃gɔ̃ʔgəgɨgɪaʊgɪɔŋgɪəgɪɛngẽhhahaihamhap̚hauhaĩheheʔhihik̚himhinhip̚hit̚hiuhiŋhiũhiũʔhiɑhiɑmhiɑnhiɑp̚hiɑt̚hiɑuhiɑuʔhiɑŋhiɑʔhiɑ̃hiɑ̃uhiɑ̃uʔhiɑ̃ʔhiɔk̚hiɔŋhiɔŋʔhiɔ̃hiəhiəʔhm̩hm̩ʔhohuhuahuaihuanhuehueʔhuihuiʔhunhut̚huɑhuɑnhuɑt̚huɑŋhuɑɪhuɑɪʔhuɑʔhuɑ̃huɑ̃ɪhuɑ̃ɪʔhuʔhãhĩhŋ̍hŋ̍ʔhũihũiʔhũʔhɑhɑk̚hɑnhɑt̚hɑuhɑuʔhɑŋhɑɪhɑɪʔhɑʔhɑ̃hɑ̃uhɑ̃ɪhɑ̃ʔhɔhɔk̚hɔnhɔŋhɔʔhɔ̃hɔ̃ʔhəhə̃ʔhɨhɪaʊhɪɔŋhɪəhɪɛnhẽhẽʔiiaŋik̚iminip̚it̚iuiuʔiŋiũiũʔiũʔʔiɑiɑk̚iɑmiɑniɑp̚iɑt̚iɑuiɑuʔiɑŋiɑʔiɑ̃iɑ̃uiɑ̃uʔiɑ̃ʔiɔk̚iɔŋiɔŋʔiɔ̃iəiəʔiʔjikkakaikamkaukaĩkekeʔkhikikik̚kimkinkip̚kit̚kiukiŋkiũkiũʔkiɑkiɑmkiɑnkiɑp̚kiɑt̚kiɑukiɑuʔkiɑŋkiɑʔkiɑ̃kiɑ̃ukiɑ̃uʔkiɔk̚kiɔŋkiɔŋʔkiɔ̃kiəkiəʔkiʔkokukuakuaikuankuekueʔkuikuiʔkunkut̚kuɑkuɑnkuɑt̚kuɑŋkuɑɪkuɑɪʔkuɑʔkuɑ̃kuɑ̃ɪkuɑ̃ɪʔkãkĩkŋ̍kŋ̍ʔkũikũiʔkũʔkɑkɑk̚kɑmkɑnkɑp̚kɑt̚kɑukɑuʔkɑŋkɑɪkɑʔkɑ̃kɑ̃ɪkɔkɔk̚kɔnkɔŋkɔ̃kɔ̃ʔkəkəʔkɨkɪaʊkɪɔŋkɪəkɪɛnkʰkʰakʰaikʰamkʰaukʰaĩkʰekʰeʔkʰikʰik̚kʰimkʰinkʰip̚kʰit̚kʰiukʰiŋkʰiũkʰiũʔkʰiɑkʰiɑk̚kʰiɑmkʰiɑnkʰiɑp̚kʰiɑt̚kʰiɑukʰiɑuʔkʰiɑŋkʰiɑʔkʰiɑ̃kʰiɑ̃ukʰiɑ̃uʔkʰiɔk̚kʰiɔŋkʰiɔŋʔkʰiɔ̃kʰiəkʰiəʔkʰiʔkʰokʰukʰuakʰuaikʰuankʰuekʰueʔkʰuikʰuiʔkʰunkʰut̚kʰuɑkʰuɑnkʰuɑt̚kʰuɑŋkʰuɑɪkʰuɑʔkʰuɑ̃kʰuʔkʰãkʰĩkʰŋ̍kʰŋ̍ʔkʰũikʰũiʔkʰũʔkʰɑkʰɑk̚kʰɑmkʰɑnkʰɑp̚kʰɑt̚kʰɑukʰɑuʔkʰɑŋkʰɑɪkʰɑʔkʰɑ̃kʰɑ̃ukʰɑ̃uʔkʰɑ̃ɪkʰɔkʰɔk̚kʰɔnkʰɔŋkʰɔ̃kʰɔ̃ʔkʰəkʰɨkʰɪaʊkʰɪɔŋkʰɪəkʰɪɛnkʰẽkʰẽʔkẽllalailamlaulaĩleleʔlilik̚limlinlip̚lit̚liuliŋliũliɑliɑmliɑnliɑp̚liɑt̚liɑuliɑuʔliɑŋliɑʔliɔk̚liɔŋliɔŋʔliəliəʔliʔlolulualuailuanluelueʔluiluiʔlunlut̚luɑluɑnluɑt̚luɑɪluɑɪʔluɑʔluʔlãlĩlŋ̍lɑlɑk̚lɑmlɑnlɑp̚lɑt̚lɑulɑuʔlɑŋlɑɪlɑɪʔlɑʔlɔlɔk̚lɔnlɔŋlɔ̃lɔ̃ʔlələʔlɨlɪaʊlɪɔŋlɪəlɪɛnlẽmamaimakmammapmatmaumaĩmemeʔmimiumiŋmiũmiɑmiɑumiɑuʔmiʔmomumuamuaimuanmuemueʔmuimuiʔmuɑmãmĩmŋ̍mŋ̍ʔmɑmɑumɑuʔmɑɪmɑʔmɑ̃umɔmɔk̚mɔnmɔŋmɔʔmɔ̃mɔ̃ʔməməʔmɨmɪkmɪɛnm̩m̩mm̩mʔm̩ʔm̩̃mẽnnanainaknamnapnatnaunaĩneneʔngininimninniuniŋniũniɑniɑmniɑnniɑp̚niɑt̚niɑuniɑuʔniɑŋniɑ̃niɑ̃ʔniɔk̚niɔŋniɔŋʔniəniəʔniʔnonunuanuainuannuenueʔnuinuiʔnunnut̚nuɑnuɑnnuɑt̚nuɑɪnuɑɪʔnuɑʔnuɑ̃nuɑ̃ɪnuɑ̃ɪʔnãnĩnŋ̍nŋ̍ʔnũinɑnɑunɑuʔnɑɪnɑʔnɑ̃unɔnɔk̚nɔnnɔŋnɔʔnɔ̃nɔ̃ʔnənəʔnɨnɪknɪɛnnẽoppapaipampappaupaĩpepeʔpipik̚pimpinpit̚piupiŋpiũpiɑk̚piɑnpiɑt̚piɑupiɑuʔpiɑŋpiɑʔpiɑ̃piəpiʔpopupuapuaipuanpuepueʔpuipuiʔpunput̚puɑpuɑnpuɑt̚puɑʔpuɑ̃puʔpãpĩpŋ̍pũipɑpɑk̚pɑnpɑt̚pɑupɑuʔpɑŋpɑɪpɑʔpɑ̃upɔpɔk̚pɔnpɔŋpɔ̃pɔ̃ʔpəpəʔpɨpɪaʊpɪəpɪɛnpʰpʰapʰaipʰampʰappʰaupʰaĩpʰepʰeʔpʰipʰik̚pʰimpʰinpʰit̚pʰiŋpʰiũpʰiɑk̚pʰiɑnpʰiɑt̚pʰiɑupʰiɑuʔpʰiɑŋpʰiɑʔpʰiɑ̃pʰiəpʰiʔpʰopʰupʰuapʰuaipʰuanpʰuepʰueʔpʰuipʰuiʔpʰunpʰut̚pʰuɑpʰuɑnpʰuɑt̚pʰuɑʔpʰuɑ̃pʰuʔpʰãpʰĩpʰŋ̍pʰŋ̍ʔpʰɑpʰɑk̚pʰɑnpʰɑt̚pʰɑupʰɑuʔpʰɑŋpʰɑɪpʰɑʔpʰɑ̃pʰɑ̃upʰɑ̃ɪpʰɔpʰɔk̚pʰɔnpʰɔŋpʰɔ̃pʰɔ̃ʔpʰəpʰəʔpʰɨpʰɪaʊpʰɪəpʰɪɛnpʰẽpẽssasaisamsausaĩseseʔsisik̚simsinsip̚sit̚siusiŋsiũsiɑsiɑk̚siɑmsiɑnsiɑp̚siɑt̚siɑusiɑuʔsiɑŋsiɑʔsiɑ̃siɑ̃ʔsiɔk̚siɔŋsiɔŋʔsiɔ̃siəsiəʔsiʔsosusuasuansuesueʔsuisuiʔsunsut̚suɑsuɑnsuɑt̚suɑɪsuɑɪʔsuɑʔsuɑ̃suɑ̃ɪsuʔsãsĩsŋ̍sŋ̍ʔsũisɑsɑk̚sɑmsɑnsɑp̚sɑt̚sɑusɑuʔsɑŋsɑɪsɑɪʔsɑʔsɑ̃sɑ̃ʔsɔsɔk̚sɔmsɔnsɔŋsɔ̃sɔ̃ʔsəsəʔsɨsɪɛnsẽttataitamtautaĩteteʔtitik̚timtintit̚tiutiuʔtiŋtiũtiɑtiɑk̚tiɑmtiɑntiɑp̚tiɑt̚tiɑutiɑuʔtiɑʔtiɑ̃tiɔk̚tiɔŋtiɔŋʔtiɔ̃tiətiəʔtiʔtotsatsaitsamtsautsaĩtsetseʔtsitsik̚tsimtsintsip̚tsit̚tsiutsiŋtsiũtsiɑtsiɑmtsiɑntsiɑp̚tsiɑt̚tsiɑutsiɑuʔtsiɑŋtsiɑʔtsiɑ̃tsiɔk̚tsiɔŋtsiɔŋʔtsiɔ̃tsiətsiəʔtsiʔtsotsutsuetsueʔtsuitsuntsut̚tsuɑtsuɑntsuɑt̚tsuɑʔtsuɑ̃tsuɑ̃ɪtsuʔtsãtsĩtsŋ̍tsŋ̍ʔtsɑtsɑk̚tsɑmtsɑntsɑp̚tsɑt̚tsɑutsɑuʔtsɑŋtsɑɪtsɑʔtsɑ̃tsɑ̃ɪtsɔtsɔk̚tsɔntsɔŋtsɔ̃tsɔ̃ʔtsətsəʔtsɨtsɪaʊtsɪətsɪɛntsʰatsʰaitsʰamtsʰautsʰaĩtsʰetsʰeʔtsʰitsʰik̚tsʰimtsʰintsʰip̚tsʰit̚tsʰiutsʰiŋtsʰiũtsʰiɑtsʰiɑk̚tsʰiɑmtsʰiɑntsʰiɑp̚tsʰiɑt̚tsʰiɑutsʰiɑuʔtsʰiɑŋtsʰiɑʔtsʰiɑ̃tsʰiɑ̃utsʰiɔk̚tsʰiɔŋtsʰiɔŋʔtsʰiɔ̃tsʰiətsʰiəʔtsʰiʔtsʰotsʰutsʰuatsʰuaitsʰuantsʰuetsʰueʔtsʰuitsʰuntsʰut̚tsʰuɑtsʰuɑntsʰuɑŋtsʰuɑɪʔtsʰuɑʔtsʰuɑ̃tsʰuʔtsʰãtsʰĩtsʰŋ̍tsʰŋ̍ʔtsʰɑtsʰɑk̚tsʰɑmtsʰɑntsʰɑp̚tsʰɑt̚tsʰɑutsʰɑuʔtsʰɑŋtsʰɑɪtsʰɑʔtsʰɑ̃tsʰɔtsʰɔk̚tsʰɔntsʰɔŋtsʰɔ̃tsʰɔ̃ʔtsʰətsʰɨtsʰɪɛntsʰẽtsẽtutuatuaituantuetuituiʔtuntut̚tuɑtuɑntuɑt̚tuɑɪtuɑʔtuɑ̃tuʔtãtĩtŋ̍tŋ̍ʔtɑtɑk̚tɑmtɑntɑp̚tɑt̚tɑutɑuʔtɑŋtɑɪtɑʔtɑ̃tɑ̃ɪtɔtɔk̚tɔmtɔntɔŋtɔ̃tɔ̃ʔtɕaĩtɕiatɕiaktɕiamtɕietɕiãtɕiũtɕiɔtɕiɔ̃tɕiẽtɕuatɕuaitɕuantɕuetɕɪɔŋtɕʰiatɕʰiaitɕʰiamtɕʰiaĩtɕʰietɕʰiiũtɕʰintɕʰiotɕʰiutɕʰiuatɕʰiuaitɕʰiuantɕʰiuetɕʰiãtɕʰiɔtɕʰiɔ̃tɕʰiẽtɕʰɪaʊtɕʰɪɔŋtətəmtəʔtɨtɪaʊtɪɔŋtɪətɪɛntʰtʰatʰaitʰamtʰautʰaĩtʰetʰeʔtʰitʰik̚tʰimtʰintʰit̚tʰiutʰiŋtʰiũtʰiɑtʰiɑmtʰiɑntʰiɑp̚tʰiɑt̚tʰiɑutʰiɑuʔtʰiɑʔtʰiɑ̃tʰiɔk̚tʰiɔŋtʰiɔŋʔtʰiətʰiʔtʰotʰutʰuatʰuaitʰuantʰuetʰueʔtʰuitʰuiʔtʰuntʰut̚tʰuɑtʰuɑntʰuɑt̚tʰuɑɪtʰuɑʔtʰuɑ̃tʰuʔtʰãtʰĩtʰŋ̍tʰŋ̍ʔtʰɑtʰɑk̚tʰɑmtʰɑntʰɑp̚tʰɑt̚tʰɑutʰɑuʔtʰɑŋtʰɑɪtʰɑʔtʰɑ̃tʰɑ̃utʰɔtʰɔk̚tʰɔntʰɔŋtʰɔ̃tʰɔ̃ʔtʰətʰəʔtʰɨtʰɪaʊtʰɪɔŋtʰɪətʰɪɛntʰẽt͡st͡sʰtẽuuauaiuanueueʔuiuiʔunut̚uɑuɑnuɑt̚uɑŋuɑɪuɑɪʔuɑʔuɑ̃uɑ̃ɪuɑ̃ɪʔuʔããũĩĩʔŋeŋeʔŋiŋik̚ŋimŋinŋip̚ŋit̚ŋiuŋiũŋiũʔŋiɑŋiɑk̚ŋiɑmŋiɑnŋiɑp̚ŋiɑt̚ŋiɑuŋiɑuʔŋiɑŋŋiɑʔŋiɑ̃ŋiɑ̃ʔŋiɔk̚ŋiɔŋŋiəŋiəʔŋiʔŋuŋueŋueʔŋuiŋuiʔŋunŋut̚ŋuɑŋuɑnŋuɑŋŋuɑɪŋuɑɪʔŋuɑʔŋuɑ̃ŋuɑ̃ɪŋuɑ̃ɪʔŋuʔŋũiŋɑŋɑk̚ŋɑp̚ŋɑt̚ŋɑuŋɑuʔŋɑŋŋɑɪŋɑɪʔŋɑ̃uŋɔŋɔk̚ŋɔmŋɔnŋɔp̚ŋɔŋŋɔ̃ʔŋəŋəʔŋ̍ŋ̍ʔũũiũiʔũʔɑɑk̚ɑuɑuʔɑŋɑɪɑɪʔɑʔɑ̃ɑ̃uɑ̃ɪɑ̃ʔɔɔk̚ɔmɔnɔpɔŋɔʔɔ̃ɔ̃ʔɕiaɕiaiɕiamɕiaĩɕieɕiiũɕinɕioɕiuɕiuaɕiuanɕiueɕiãɕiɔɕiɔ̃ɕiẽɕuaiɕɪaʊɕɪɔŋəəŋəʔə̃ɛɨɪaʊɪɔŋɪəɪɛnʑaiʑiʑiaʑiakʑiamʑieʑimʑinʑioʑiuʑiãʑiŋ̍ʑiɔʑiɔ̃ʑiẽʑueʑɨʑɪaʊʑɪɔŋʑɪɛnʥiʥik̚ʥimʥinʥip̚ʥit̚ʥiuʥiɑʥiɑmʥiɑnʥiɑp̚ʥiɑt̚ʥiɑuʥiɑuʔʥiɑŋʥiɑʔʥiɔk̚ʥiɔŋʥiɔŋʔʥiəʥuʥueʥuiʥunʥuɑʥuɑʔẽẽʔ"
# DEFAULT SET OF IPA PHONEMES
# Phonemes definition (All IPA characters)
_vowels = "iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ"
_non_pulmonic_consonants = "ʘɓǀɗǃʄǂɠǁʛ"
_pulmonic_consonants = "pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ"
_suprasegmentals = "ˈˌːˑ"
_other_symbols = "ʍwɥʜʢʡɕʑɺɧʲ"
_diacrilics = "ɚ˞ɫ"
#_phonemes = _vowels + _non_pulmonic_consonants + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics
_phonemes = _vowels + _non_pulmonic_consonants + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics + "1，23456758。" + addText


class BaseVocabulary:
    """Base Vocabulary class.

    This class only needs a vocabulary dictionary without specifying the characters.

    Args:
        vocab (Dict): A dictionary of characters and their corresponding indices.
    """

    def __init__(self, vocab: Dict, pad: str = None, blank: str = None, bos: str = None, eos: str = None):
        self.vocab = vocab
        self.pad = pad
        self.blank = blank
        self.bos = bos
        self.eos = eos

    @property
    def pad_id(self) -> int:
        """Return the index of the padding character. If the padding character is not specified, return the length
        of the vocabulary."""
        return self.char_to_id(self.pad) if self.pad else len(self.vocab)

    @property
    def blank_id(self) -> int:
        """Return the index of the blank character. If the blank character is not specified, return the length of
        the vocabulary."""
        return self.char_to_id(self.blank) if self.blank else len(self.vocab)

    @property
    def bos_id(self) -> int:
        """Return the index of the bos character. If the bos character is not specified, return the length of the
        vocabulary."""
        return self.char_to_id(self.bos) if self.bos else len(self.vocab)

    @property
    def eos_id(self) -> int:
        """Return the index of the eos character. If the eos character is not specified, return the length of the
        vocabulary."""
        return self.char_to_id(self.eos) if self.eos else len(self.vocab)

    @property
    def vocab(self):
        """Return the vocabulary dictionary."""
        return self._vocab

    @vocab.setter
    def vocab(self, vocab):
        """Set the vocabulary dictionary and character mapping dictionaries."""
        self._vocab, self._char_to_id, self._id_to_char = None, None, None
        if vocab is not None:
            self._vocab = vocab
            self._char_to_id = {char: idx for idx, char in enumerate(self._vocab)}
            self._id_to_char = dict(enumerate(self._vocab))

    @staticmethod
    def init_from_config(config, **kwargs):
        """Initialize from the given config."""
        if config.characters is not None and "vocab_dict" in config.characters and config.characters.vocab_dict:
            return (
                BaseVocabulary(
                    config.characters.vocab_dict,
                    config.characters.pad,
                    config.characters.blank,
                    config.characters.bos,
                    config.characters.eos,
                ),
                config,
            )
        return BaseVocabulary(**kwargs), config

    def to_config(self) -> "CharactersConfig":
        return CharactersConfig(
            vocab_dict=self._vocab,
            pad=self.pad,
            eos=self.eos,
            bos=self.bos,
            blank=self.blank,
            is_unique=False,
            is_sorted=False,
        )

    @property
    def num_chars(self):
        """Return number of tokens in the vocabulary."""
        return len(self._vocab)

    def char_to_id(self, char: str) -> int:
        """Map a character to an token ID."""
        try:
            return self._char_to_id[char]
        except KeyError as e:
            raise KeyError(f" [!] {repr(char)} is not in the vocabulary.") from e

    def id_to_char(self, idx: int) -> str:
        """Map an token ID to a character."""
        return self._id_to_char[idx]


class BaseCharacters:
    """🐸BaseCharacters class

        Every new character class should inherit from this.

        Characters are oredered as follows ```[PAD, EOS, BOS, BLANK, CHARACTERS, PUNCTUATIONS]```.

        If you need a custom order, you need to define inherit from this class and override the ```_create_vocab``` method.

        Args:
            characters (str):
                Main set of characters to be used in the vocabulary.

            punctuations (str):
                Characters to be treated as punctuation.

            pad (str):
                Special padding character that would be ignored by the model.

            eos (str):
                End of the sentence character.

            bos (str):
                Beginning of the sentence character.

            blank (str):
                Optional character used between characters by some models for better prosody.

            is_unique (bool):
                Remove duplicates from the provided characters. Defaults to True.
    el
            is_sorted (bool):
                Sort the characters in alphabetical order. Only applies to `self.characters`. Defaults to True.
    """

    def __init__(
        self,
        characters: str = None,
        punctuations: str = None,
        pad: str = None,
        eos: str = None,
        bos: str = None,
        blank: str = None,
        is_unique: bool = False,
        is_sorted: bool = True,
    ) -> None:
        self._characters = characters
        self._punctuations = punctuations
        self._pad = pad
        self._eos = eos
        self._bos = bos
        self._blank = blank
        self.is_unique = is_unique
        self.is_sorted = is_sorted
        self._create_vocab()

    @property
    def pad_id(self) -> int:
        return self.char_to_id(self.pad) if self.pad else len(self.vocab)

    @property
    def blank_id(self) -> int:
        return self.char_to_id(self.blank) if self.blank else len(self.vocab)

    @property
    def eos_id(self) -> int:
        return self.char_to_id(self.eos) if self.eos else len(self.vocab)

    @property
    def bos_id(self) -> int:
        return self.char_to_id(self.bos) if self.bos else len(self.vocab)

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, characters):
        self._characters = characters
        self._create_vocab()

    @property
    def punctuations(self):
        return self._punctuations

    @punctuations.setter
    def punctuations(self, punctuations):
        self._punctuations = punctuations
        self._create_vocab()

    @property
    def pad(self):
        return self._pad

    @pad.setter
    def pad(self, pad):
        self._pad = pad
        self._create_vocab()

    @property
    def eos(self):
        return self._eos

    @eos.setter
    def eos(self, eos):
        self._eos = eos
        self._create_vocab()

    @property
    def bos(self):
        return self._bos

    @bos.setter
    def bos(self, bos):
        self._bos = bos
        self._create_vocab()

    @property
    def blank(self):
        return self._blank

    @blank.setter
    def blank(self, blank):
        self._blank = blank
        self._create_vocab()

    @property
    def vocab(self):
        return self._vocab

    @vocab.setter
    def vocab(self, vocab):
        self._vocab = vocab
        self._char_to_id = {char: idx for idx, char in enumerate(self.vocab)}
        self._id_to_char = dict(enumerate(self.vocab))

    @property
    def num_chars(self):
        return len(self._vocab)

    def _create_vocab(self):
        _vocab = self._characters
        if self.is_unique:
            _vocab = list(set(_vocab))
        if self.is_sorted:
            _vocab = sorted(_vocab)
        _vocab = list(_vocab)
        _vocab = [self._blank] + _vocab if self._blank is not None and len(self._blank) > 0 else _vocab
        _vocab = [self._bos] + _vocab if self._bos is not None and len(self._bos) > 0 else _vocab
        _vocab = [self._eos] + _vocab if self._eos is not None and len(self._eos) > 0 else _vocab
        _vocab = [self._pad] + _vocab if self._pad is not None and len(self._pad) > 0 else _vocab
        self.vocab = _vocab + list(self._punctuations)
        if self.is_unique:
            duplicates = {x for x in self.vocab if self.vocab.count(x) > 1}
            assert (
                len(self.vocab) == len(self._char_to_id) == len(self._id_to_char)
            ), f" [!] There are duplicate characters in the character set. {duplicates}"

    def char_to_id(self, char: str) -> int:
        try:
            return self._char_to_id[char]
        except KeyError as e:
            raise KeyError(f" [!] {repr(char)} is not in the vocabulary.") from e

    def id_to_char(self, idx: int) -> str:
        return self._id_to_char[idx]

    def print_log(self, level: int = 0):
        """
        Prints the vocabulary in a nice format.
        """
        indent = "\t" * level
        logger.info("%s| Characters: %s", indent, self._characters)
        logger.info("%s| Punctuations: %s", indent, self._punctuations)
        logger.info("%s| Pad: %s", indent, self._pad)
        logger.info("%s| EOS: %s", indent, self._eos)
        logger.info("%s| BOS: %s", indent, self._bos)
        logger.info("%s| Blank: %s", indent, self._blank)
        logger.info("%s| Vocab: %s", indent, self.vocab)
        logger.info("%s| Num chars: %d", indent, self.num_chars)

    @staticmethod
    def init_from_config(config: "Coqpit"):  # pylint: disable=unused-argument
        """Init your character class from a config.

        Implement this method for your subclass.
        """
        # use character set from config
        if config.characters is not None:
            return BaseCharacters(**config.characters), config
        # return default character set
        characters = BaseCharacters()
        new_config = replace(config, characters=characters.to_config())
        return characters, new_config

    def to_config(self) -> "CharactersConfig":
        return CharactersConfig(
            characters=self._characters,
            punctuations=self._punctuations,
            pad=self._pad,
            eos=self._eos,
            bos=self._bos,
            blank=self._blank,
            is_unique=self.is_unique,
            is_sorted=self.is_sorted,
        )


class IPAPhonemes(BaseCharacters):
    """🐸IPAPhonemes class to manage `TTS.tts` model vocabulary

    Intended to be used with models using IPAPhonemes as input.
    It uses system defaults for the undefined class arguments.

    Args:
        characters (str):
            Main set of case-sensitive characters to be used in the vocabulary. Defaults to `_phonemes`.

        punctuations (str):
            Characters to be treated as punctuation. Defaults to `_punctuations`.

        pad (str):
            Special padding character that would be ignored by the model. Defaults to `_pad`.

        eos (str):
            End of the sentence character. Defaults to `_eos`.

        bos (str):
            Beginning of the sentence character. Defaults to `_bos`.

        blank (str):
            Optional character used between characters by some models for better prosody. Defaults to `_blank`.

        is_unique (bool):
            Remove duplicates from the provided characters. Defaults to True.

        is_sorted (bool):
            Sort the characters in alphabetical order. Defaults to True.
    """

    def __init__(
        self,
        characters: str = _phonemes,
        punctuations: str = _punctuations,
        pad: str = _pad,
        eos: str = _eos,
        bos: str = _bos,
        blank: str = _blank,
        is_unique: bool = False,
        is_sorted: bool = True,
    ) -> None:
        super().__init__(characters, punctuations, pad, eos, bos, blank, is_unique, is_sorted)

    @staticmethod
    def init_from_config(config: "Coqpit"):
        """Init a IPAPhonemes object from a model config

        If characters are not defined in the config, it will be set to the default characters and the config
        will be updated.
        """
        # band-aid for compatibility with old models
        if "characters" in config and config.characters is not None:
            if "phonemes" in config.characters and config.characters.phonemes is not None:
                config.characters["characters"] = config.characters["phonemes"]
            return (
                IPAPhonemes(
                    characters=config.characters["characters"],
                    punctuations=config.characters["punctuations"],
                    pad=config.characters["pad"],
                    eos=config.characters["eos"],
                    bos=config.characters["bos"],
                    blank=config.characters["blank"],
                    is_unique=config.characters["is_unique"],
                    is_sorted=config.characters["is_sorted"],
                ),
                config,
            )
        # use character set from config
        if config.characters is not None:
            return IPAPhonemes(**config.characters), config
        # return default character set
        characters = IPAPhonemes()
        new_config = replace(config, characters=characters.to_config())
        return characters, new_config


class Graphemes(BaseCharacters):
    """🐸Graphemes class to manage `TTS.tts` model vocabulary

    Intended to be used with models using graphemes as input.
    It uses system defaults for the undefined class arguments.

    Args:
        characters (str):
            Main set of case-sensitive characters to be used in the vocabulary. Defaults to `_characters`.

        punctuations (str):
            Characters to be treated as punctuation. Defaults to `_punctuations`.

        pad (str):
            Special padding character that would be ignored by the model. Defaults to `_pad`.

        eos (str):
            End of the sentence character. Defaults to `_eos`.

        bos (str):
            Beginning of the sentence character. Defaults to `_bos`.

        is_unique (bool):
            Remove duplicates from the provided characters. Defaults to True.

        is_sorted (bool):
            Sort the characters in alphabetical order. Defaults to True.
    """

    def __init__(
        self,
        characters: str = _characters,
        punctuations: str = _punctuations,
        pad: str = _pad,
        eos: str = _eos,
        bos: str = _bos,
        blank: str = _blank,
        is_unique: bool = False,
        is_sorted: bool = True,
    ) -> None:
        super().__init__(characters, punctuations, pad, eos, bos, blank, is_unique, is_sorted)

    @staticmethod
    def init_from_config(config: "Coqpit"):
        """Init a Graphemes object from a model config

        If characters are not defined in the config, it will be set to the default characters and the config
        will be updated.
        """
        if config.characters is not None:
            # band-aid for compatibility with old models
            if "phonemes" in config.characters:
                return (
                    Graphemes(
                        characters=config.characters["characters"],
                        punctuations=config.characters["punctuations"],
                        pad=config.characters["pad"],
                        eos=config.characters["eos"],
                        bos=config.characters["bos"],
                        blank=config.characters["blank"],
                        is_unique=config.characters["is_unique"],
                        is_sorted=config.characters["is_sorted"],
                    ),
                    config,
                )
            return Graphemes(**config.characters), config
        characters = Graphemes()
        new_config = replace(config, characters=characters.to_config())
        return characters, new_config


if __name__ == "__main__":
    gr = Graphemes()
    ph = IPAPhonemes()
    gr.print_log()
    ph.print_log()
