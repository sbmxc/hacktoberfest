from time import sleep


frame_color = '\u001b[32m'
cursor_move = '\u001b[25A'
discard_changes = '\u001b[0m'
planet_frame_1 = """
                _-o#&&*''''?d:>b\\_
              _o/'`''  '',, dMF9MMMMMHo_
           .o&#'        `'MbHMMMMMMMMMMMHo.
         .o'' '         vodM*$&&HMMMMMMMMMM?.
        ,'              $M&ood,~'`(&##MMMMMMH\\
       /               ,MMMMMMM#b?#bobMMMMHMMML
      &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
     ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
    |               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
    $H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
    ]MMH#             ''*''''*#MMMMMMMMMMMMM'    -
    MMMMMb_                   |MMMMMMMMMMMP'     :
    HMMMMMMMHo                 `MMMMMMMMMT       .
    ?MMMMMMMMP                  9MMMMMMMM}       -
    -?MMMMMMM                  |MMMMMMMMM?,d-    '
     :|MMMMMM-                 `MMMMMMMT .M|.   :
      .9MMM[                    &MMMMM*' `'    .
       :9MMk                    `MMM#'        -
         &M}                     `          .-
          `&.                             .
            `~,   .                     ./
                . _                  .-P
                  '`--._,dd###pp='''
"""

planet_frame_2 = """
                  .ovr:HMM#?:`' >b\\_
              .,:&Hi' `'   '' \\\\|&bSMHo_
            oHMMM#*}          `?&dMMMMMMHo.
         .dMMMH'''''           ,oHH*&&9MMMM?.
        ,MMM*'                 `*M\\bd<|'*&#MH\\
       dHH?'                   :MMMMMM#bd#odMML
      H' |\\                  `dMMMMMMMMMMMMMM9Mk
     JL/'7+,.                `MMMMMMMMMMMMMMMH9ML
    -`Hp     '               |MMMMMMMMMMMMMMMMHH|:
    :  \\\\#M#d?                `HMMMMMMMMMMMMMMMMH.
    .   JMMMMM##,              ``*''''*#MMMMMMMMH
    -. ,MMMMMMMM6o_                    |MMMMMMMM':
    :  |MMMMMMMMMMMMMb\\                 TMMMMMMT :
    .   ?MMMMMMMMMMMMM'                 :MMMMMM|.`
    -    ?HMMMMMMMMMM:                  HMMMMMM\\|:
     :     9MMMMMMMMH'                 `MMMMMP.P.
      .    `MMMMMMT''                   HMMM*''-
       -    TMMMMM'                     MM*'  -
        '.   HMM#                            -
          -. `9M:                          .'
            -. `b,,    .                . '
              '-\\   .,               .-`
                  '-:b~\\\\_,oddq==--
"""
planet_frame_3 = """
                  _oo##'9MMHb':'-,o_
              .vM':HH$'    '''  '' -\\7*_
           .oHMMMHMH#9:          '\\bMMMMHo.
         . ,dMMMMMMMMMMM'`' `           ?MP?.
        . |MMMMMMMMMMM'                 `'$b&\\
       -  |MMMMHH##M'                     HMMH?
      -   TTMM|    >..                   \\MMMMMH
     :     |MM\\,#-''$~b\\.                `MMMMMM+
    .       ``'H&#        -               &MMMMMM|
    :            *\\v,#MHddc.              `9MMMMMb
    .               MMMMMMMM##\\             `'':HM
    -          .  .HMMMMMMMMMMRo_.              |M
    :             |MMMMMMMMMMMMMMMM#\\           :M
    -              `HMMMMMMMMMMMMMMM'           |T
    :               `*HMMMMMMMMMMMM'            H'
     :                 MMMMMMMMMMM|            |T
      .                MMMMMMMM?'             ./
      `.               MMMMMMH'              ./
        -.            |MMMH#'                .
          .           `MM*                . '
            -.         #M: .    .       .-
              ` .         .,         .-
                  '-.-~ooHH__,,v~--
"""
planet_frame_4 = """
                  _,\\?dZkMHF&$*q#b..
              .//9MMMMMMM?:'HM\\\\'`-''`..
           ..`  :MMMMMMMMMMHMMMMH?_    `-\\
         .     .dMMMMMMMMMMMMMM''''       `\\.
        .      |MMMMMMMMMMMMMR              \\\\
       -        T9MMMMMHH##M'                `?
      :          (9MMM'    !':.               &k
     .:            HMM\\_?p '':-b\\.            `ML
    -                '''H&#,       :           |M|
    :                     ?\\,\\dMH#b#.           9b
    :                        |MMMMMMM##,        `*
    :                   .   +MMMMMMMMMMMo_       -
    :                       HMMMMMMMMMMMMMM#,    :
    :                        9MMMMMMMMMMMMMH'    .
    : .                       *HMMMMMMMMMMP     .'
     :                          MMMMMMMMMH'     .
      -                        :MMMMMMM'`      .
      `.                       9MMMMM*'       -
        -.                    {MMM#'         :
          -                  |MM'          .'
           `.                &M'..  .   ..'
              ' .             ._     .-
                  '-. -voboo#&:,-.-
"""
planet_frame_5 = """
                  _\\oo\\?ddk9MRbS>v\\_
              ..:>*''MMMMMMMMM:?|H?$?-.
           ..- -     'HMMMMMMMMMMHMMMH\\_-.
         .            dMMMMMMMMMMMMMMT'    .
        .             TMMMMMMMMMMMMMM       `.
       -               `&HMMMMMM#H#H:         .
      -                 `\\7HMMH     |\\.        .
     :    `                 HMM\\_?c`''+?\\..     :
    -                         '``#&#|      .     -
    :                              `?,\\#MHdb.    .
    :                                 |MMMMMH#.  :
    :                            .   ,HMMMMMMMb, -
    : '                              4MMMMMMMMMMH`
    :   .                             9MMMMMMMMMT-
    :.`                               `#MMMMMMMH '
     :      '                           HMMMMMH':
      -                                |MMMMH' -
      `:                              |MMMH*' .'
        '?                           dMM#'   .
          \\.                       .dH'    .'
            -.                    ,M'-  ..'
              ` .                .. ..-`
                  '-. .\\ooooboo<^.-`
"""
planet_frame_6 = """
                  _o\\:,??\\??MR9#cb\\_
              .v/''':&#''#HMMMMMMM$?*d\\.
           ..~' - -`      `'#MMMMMMMMMMMHv.
         .-'                 HMMMMMMMMMMMR!.
        :                    `9MMMMMMMMMMM| -.
       .                       `*9MMMMMH##|   .
      -                          `(#MMH   `:,  .
     :           '|                 `HMb_>/'|\\,.:
    .'                                `''#&b   - .
    :                                      ?\\oHH?.
    :                                        !MMM&
    :  .                                  .  HMMMM
    /.      -                               -MMMMM
    \\`.                                      9MMMP
    :. .  . -                                |MMM'
     \\... '                                  .MMT
      &.                                    .dMP
       \\,                                  .HM*
        \\. `\\.                            ,H&'
         `- `| -                        ,&':
           `.                         ,/\\ '
              '-..                  _.-
                  '---.._\\o,oov+--''
"""
planet_frame_7 = """
                  _,oc>?_:b?o?HH#b\\_
              .v/99*''' '*H#''*HMMMMMZ,_
            oH* /'   -   '      '`#MMMMM#o.
         ./*>-                     `MMMMMMMb
        ,b/'                        `#MMMMMMM\\
       :'                             ``HMMMMb:
      /-                                `|&MH `\\
     /                   `-.               |Hb??\\
    ,-  '                                    '`&,.
    1                                           \\}
    !.                                           T
    $,.                                        . 1
    ?`M??.                                       M
    ?.::| '\\        -                            ?
     M?&.    .   .  -                           ,'
     9MMH\\   ..  '           `                  .
      HMMM#.                                   :'
       9#MMb                                 ..
        -:'#     `b.                        .-
          . `    {!                        /
            -                           ,-'
              ' .                    .-
                 ```^==\\_.,,,ov--\\-`
"""
planet_frame_8 = """
                  _,o#bH\\??::?o?cbo_
              .o#MH#**SH''' '`*H#'*#MHo_
            oHMMMH^  ^'    -  `      '*HHo.
         .dMMM#'>>-                     `HM?.
        ,MH:R_o/                         `*MH\\
       dMM' '                               'ML
      HMR! '                                 `#k
     d&'.                          -.          `L
    :M ::     `                                 `-
    /| !|                                        -
    k.$-'                                        :
    }9R:!,,_.                                    .
    \\::\\':`*M#\\-'.                               -
    : '''..:'!`\\  '-          -                  `
    -   ,HMb.H|      .    _   -                 .'
     : ,MMMMMMMb.    ..                         .
      .`HMMMMMMMM?                             .
      `.`9M#*HMMMM                            :
        -.'   '##*      `b,                  .
          .      `     ,/'                 .'
           ` .                          ..'
               - .                  ..-
                  '`*#d##c.._\\v----`
"""
planet_frame_9 = """
                  _oo#H&d#b?\\b:_>>\\_
              .oHMMMMMMH*'*9R''-``*#P\\-_
            oHMMMMMMMMM$  .'       '   `^-
         .dMMMMMMMMH*',?-                 '\\.
        ,MMMMMMM:?}.,d'                     `.
       dMMMMMMMH  /''                         :
      HMMMMMMM&' -                             -
     dPTMMP>' :                           -.    :
    |? -MM}  .\\                                  .
    J' ::*'  -$L                                 .
    :  ?b .,H- '                                 :
    -  |6.&MP:: !.,_.                            -
    :   `\\:: '' '`:'MM#,-^,            -         :
    -     ````:' _.:'?``\\   `-                   .
    :         .?bMML.]#        -   _  `      .  .'
     -      .o#MMMMMMMMH\\     \\.          .     .
      -     `HMMMMMMMMMMMH                     :
      `.     `HMM#*#MMMMMH'                   -
        -.     '    ``##*'      i+           :
          -            `'     v/'          .'
           `-                           ..'
              ' .                    .-
                  '`*##HMH##:__,-.-`
"""
planet_frame_10 = """
                  _,dd#HMb&dHo?\\?:\\_
              .oHMMMMMMMMMMMH***9P'`'\\v.
            oHMMMMMMMMMMMMMMM>  `'      -.
         .dMMMMMMMMMMMMMMMH*'|~-'          .
        ,MMMMMMMMMMMMM6>`H._,&              -.
       dMMMMMMMMMMMMMMM|  `'                  .
      H*MMMMMMMMMMMMMH&. -                     .
     d' HMM''&MMMPT'' :.                      `.-
    ,'  MP   `TMMM,   |:        .                -
    |   #:    ? *'   : &L                        :
    !   `'   /?H   ,#r `'                        :
    .         ?M: HMM^<~->,o._                   :
    :          `9:::'`*-``':`9MHb,|-,         '  :
    .             `'''':' :_ ''!'^.  `|          :
    `.                 _dbHM6_|H.      .   . '  .'
     \\              _odHMMMMMMMMH,    ..  `     :
     `-             |MMMMMMMMMMMMM|            :
      `.             9MMH**#MMMMMH'           :
        -.            '     '?##'      d     :
          .                    '    ,/'    .'
           `..                          ..'
              `  .                   .-
                  '`'#HHMMMMM#<>..-`
"""
planet_frame_11 = """
                  _,,>#b&HMHd&&bb>\\_
              _oHMMMMMMMMMMMMMMMMH**H:.
            oHMMMMMMMMMMMMMMMMMMMM#v`?  `.
         .dMMMMMMMMMMMMMMMMMMMMMMH*`+|     .
        ,MMMMMMMMMMMMMMMMMMMMMb|?+.,H       -.
       ddHMMMMMMMMMMMMMMMMMMMMMb  `'          .
      HMMkZ**HMMMMMMMMMMMMMMMMH\\  -   .        :
     dTMMM*  `9MMMP''*MMMMPT'` ..               :
    |M6H''    4MP'   `'HMMM|   !|.      .        .
    1MHp'      #L      $ *''  .-:&.              .
    MMM'        '     q:H.  .o#-``'              :
    MM'                ?H?.|MMH::::-o,_.         -
    M[                  `*?:::'|` `'`:9MH\\~-.    `
    &M.                     '''`'^'.:.`?'`. '|  -:
    `M|d,                       .dbHM[.1?     .. :
     9||| .                  _obMMMMMMMMH,   .  :
      H.^                    MMMMMMMMMMMM}     -
       \\                     |MMH#*HMMMMH'    .'
        .                    `      `#*'   ,:-
         `                           '' .-'.
           `.                           .-
              '- .                   .-`
                  '`\\bqHMMMMMMHHb--`
"""
planet_frame_12 = """
                  _,<_:&S6dHHHb&bb\\_
              .odHMMMMMMMMMMMMMMMMMMM}-_
           .oHMMMMMMMMMMMMMMMMMMMMMMMM#d:.
          ?9MMMMMMMMMMMMMMMMMMMMMMMMMMMH-$ .
        ,::dHMMMMMMMMMMMMMMMMMMMMMMMMH:\\.?? -.
       dMdboHMMHMMMMMMMMMMMMMMMMMMMMMMH, '    .
      HMMMM7MMMb$R***MMMMMMMMMMMMMMMMMH\\ -     .
     dMMMMM/MMMMM*   `$MMMM*''*MMMM?&'  .       :
    |MMMMMMb1H*'       HMP'    '9MMM|   &.    .  .
    dMMMMMMM##~`       `#\\      |.`*'  .-9.      :
    9MMMMMMMM*           `     |v7?  .,H `' `    :
    SMMMMMMH'                   '9M_-MMH::-\\v_   :
    :HMMMMM                       `\\_:''|'`':9Mv\\.
    -|MMMMM,                         ''`'`':.`?\\ \\
    `:MMMMM}.d}                         .?bM6,|  |
     :?MMM6  M|  .                   .,oHMMMMM| /
      .?MMM- `'                      &MMMMMMMM|.
       -`HM-                         HMH#*MMM?:
        '.                           '   `#*:`
          -                              -'/
           ` .                          . '
              ` .                    . `
                  '--##HH#HMMMHH#''`
"""
planet_frame_13 = """
                  .-:?,Z?:&$dHH##b\\_
               ,:bqRMMMMMMMMMMMMMMMMMHo.
            .?HHHMMMMMMMMMMMMMMMMMMMMMMMHo.
          -o/*M9MMMMMMMMMMMMMMMMMMMMMMMMMMMv
        .:H\\b\\'|?#HHMMMMMMMMMMMMMMMMMMMMMM6?Z\\
       .?MMMHbdbbodMMMMHMMMMMMMMMMMMMMMMMMMM\\':
      :MMMMMMMMMMM7MMMMb?6P**#MMMMMMMMMMMMMMM_ :
     \\MMMMMMMMMMMMb^MMMMMM?   `*MMMM*'`MMMR<' . -
    .1MMMMMMMMMMMMMb]M#''       9MR'   `?MMb  \\. :
    -MMMMMMMMMMMMMMMH##|`        *&.     |`*' .\\ .
    -?''*MMMMMMMMMMMMM'            '    |?b  ,}' :
    :    MMMMMMMMMMH'                    `M_|M}r\\?
    .    `MMMMMMMMM'                      `$_:`''H
    -     TMMMMMMMM,                        ''``::
    :     {MMMMMMMM| oH|                      .#M-
     :    `9MMMMMM' .MP   .                 ,oMMT
      .     HMMMMP'  `'                    ,MMMP
       -     `MMH'                         HH9*
        '.    `                           ` .'
          -                               . '
           ` .               -          .-
              ` .                    .-
                  ' -==pHMMH##HH#'''
"""
frames = [
    planet_frame_1,
    planet_frame_2,
    planet_frame_3,
    planet_frame_4,
    planet_frame_5,
    planet_frame_6,
    planet_frame_7,
    planet_frame_8,
    planet_frame_9,
    planet_frame_10,
    planet_frame_11,
    planet_frame_12,
    planet_frame_13
]

print(frame_color, frames[0])
sleep(1)
for frame in frames[1:-1]:
    print(cursor_move + frame)
    sleep(1)

print(cursor_move, frames[-1], discard_changes)
