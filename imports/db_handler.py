import marshal, base64
exec(base64.b32decode("NFWXA33SOQQHG4LMNF2GKMZAMFZSA3DJORSQUZTSN5WSA2LNOBXXE5DTEBUW24DPOJ2CAZ3MN5RGC3DTBJUW24DPOJ2CA43ZOMFAUCTDNRQXG4ZAIRBEQYLOMRWGK4R2BIFCAIBAEBSGKZRAL5PWS3TJORPV6KDTMVWGMKJ2BIQCAIBAEAQCAIDUOJ4TUCRAEAQCAIBAEAQCAIBAEBZWK3DGFZRW63RAHUQGY2LUMUXGG33ONZSWG5BIM5WG6YTBNRZS45TBOJZS4ZDCL5YGC5DIFEFCAIBAEAQCAIBAEAQCAIDTMVWGMLTDOVZCAPJAONSWYZROMNXW4LTDOVZHG33SFAUQUIBAEAQCAIBAEBSXQY3FOB2CA3DJORSS4RLSOJXXEIDBOMQGKOQKEAQCAIBAEAQCAIBAEAQHA4TJNZ2CQISBNYQGK4TSN5ZCA33DMN2XE4TFMQ5CELBAMUXGC4THONNTAXJJBIQCAIBAEAQCAIBAEAQCA43ZOMXGK6DJOQUCSCQKEAQCAIDEMVTCAZ3FORPWM5LMNRPWIZLUMFUWY4ZIONSWYZRJHIFCAIBAEAQCAIBAOJSXI5LSNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKBCKNCUYRKDKQQCUICGKJHU2ICNMFWHOYLSMVZSEKJOMZSXIY3IMFWGYKBJBIFCAIBAEBSGKZRAM5SXIX3QMFZHI2LBNRPWIZLUMFUWY4ZIONSWYZRJHIFCAIBAEAQCAIBAOJSXI5LSNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKBCKNCUYRKDKQQESRBMEBKFSUCFFQQEYQKOI5KUCR2FFQQECUSDJBEVIRKDKRKVERJMEBIEYQKUIZHVETJMEBHECTKFEBDFET2NEBGWC3DXMFZGK4ZCFEXGMZLUMNUGC3DMFAUQUCRAEAQCAZDFMYQGOZLUL5WWC3C7NRUXG5BIONSWYZRJHIFCAIBAEAQCAIBAOJSXI5LSNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKBCKNCUYRKDKQQESRBMEBHECTKFFQQFIWKQIUQEM4TPNUQE2YLMO5QXEZLTEIUS4ZTFORRWQYLMNQUCSCQKEAQCAIDEMVTCAZ3FORPW2YLML5XGC3LFOMUHGZLMMYUTUCQKEAQCAIBAEAQCAIZAKNYWY2LUMUZSA4TFOR2XE3TTEBQSA5DVOBWGKIDFOZSW4IDJMYQGCIDTNFXGO3DFEB3GC3DVMUQGS4ZAOJSXI5LSNZSWICRAEAQCAIBAEAQCGICXMUQHK43FEB4FWMC5EBTG64RAPAQHI3ZAOVXHAYLDNMQHI2DFEB2HK4DMMVZQUIBAEAQCAIBAEBZGK5DVOJXCAW3WMFWFWMC5EBTG64RAOZQWYIDJNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKBCKNCUYRKDKQQE4QKNIUQEMUSPJUQE2YLMO5QXEZLTEIUS4ZTFORRWQYLMNQUCSXIKBIQCAIBAMRSWMIDHMV2F63LBNRPXIYLHOMUHGZLMMYUTUCRAEAQCAIBAEAQHEZLUOVZG4IC3OZQWYWZQLUQGM33SEB3GC3BANFXCA43FNRTC4Y3VOIXGK6DFMN2XIZJIEJJUKTCFINKCARCJKNKESTSDKQQFIQKHKMQEM4TPNUQE2YLMO5QXEZLTEBLUQRKSIUQFIQKHKMQESUZAJZHVIICOKVGEYIRJFZTGK5DDNBQWY3BIFFOQUCRAEAQCAZDFMYQGOZLUL5WWC3C7NFXGM3ZIONSWYZRMEBWWSZBJHIFCAIBAEAQCAIBAOJSXI5LSNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKBCKNCUYRKDKQQFIWKQIUWCATSBJVCSYICWIVJFGSKPJYWCAQKVKREE6URMEBGECTSHKVAUORJMEBCECVCFFQQECUSDJBEVIRKDKRKVERJMEBIEYQKUIZHVETJMEBKECR2TEBDHE33NEBGWC3DXMFZGK4ZAK5EEKUSFEBEUIIB5EIQCWIDTORZCQ3LJMQUSSLTGMV2GG2DBNRWCQKIKBIQCAIBAMRSWMIDROVSXE6JIONSWYZRMEBYXKZLSPEWCA4DBOJQW2PJHE4UTUCRAEAQCAIBAEAQGSZRAM5WG6YTBNRZS45TBOJZS4RCFIJKUOX2MIVLEKTBANFZSAMR2BIQCAIBAEAQCAIBAEAQCA4DSNFXHIKDMN5RWC3DTFAUSSCRAEAQCAIBAEAQHI4TZHIFCAIBAEAQCAIBAEAQCAIDJMYQHAYLSMFWSA2LTEBXG65BAE4TTUCRAEAQCAIBAEAQCAIBAEAQCAIBAOJSXI5LSNYQHGZLMMYXGG5LSFZSXQZLDOV2GKKDROVSXE6JMEBYGC4TBNUQGSZRAOR4XAZJIOBQXEYLNFEQGS4ZANRUXG5BAMVWHGZJALNYGC4TBNVOSSLTGMV2GG2DBNRWCQKIKEAQCAIBAEAQCAIBAEAQGK3DTMU5AUIBAEAQCAIBAEAQCAIBAEAQCAIDSMV2HK4TOEBZWK3DGFZRXK4ROMV4GKY3VORSSQ4LVMVZHSKJOMZSXIY3IMFWGYKBJBIQCAIBAEAQCAIDFPBRWK4DUEBWGS5DFFZCXE4TPOIQGC4ZAMU5AUIBAEAQCAIBAEAQCAIBAOBZGS3TUFAREC3RAMVZHE33SEBXWGY3VOJZGKZB2EIWCAZJOMFZGO423GBOSSCRAEAQCAIBAEAQCAIBAEBZXS4ZOMV4GS5BIFEFAUIBAEAQGIZLGEBRWY33TMVPWG33ONZSWG5DJN5XCQ43FNRTCSOQKEAQCAIBAEAQCA5DSPE5AUIBAEAQCAIBAEAQCAIBAONSWYZROMN2XELTDNRXXGZJIFEFCAIBAEAQCAIBAEAQCAIDTMVWGMLTDN5XC4Y3MN5ZWKKBJBIQCAIBAEAQCAIBAEAQCA4TFOR2XE3QKEAQCAIBAEAQCAZLYMNSXA5BANRUXIZJOIVZHE33SEBQXGIDFHIFCAIBAEAQCAIBAEAQCAIDQOJUW45BIEJAW4IDFOJZG64RAN5RWG5LSOJSWIORCFQQGKLTBOJTXGWZQLUUQUIBAEAQCAIBAEAQCAIBAON4XGLTFPBUXIKBJBIFCAIBAEBSGKZRAOJSW4ZLXL5RW63TOMVRXI2LPNYUHGZLMMYUTUCRAEAQCAIBAEAQHI4TZHIFCAIBAEAQCAIBAEAQCAIDTMVWGMLTDN5XCAPJANRUXIZJOMNXW43TFMN2CQZ3MN5RGC3DTFZ3GC4TTFZSGEX3QMF2GQKIKEAQCAIBAEAQCAIBAEAQHGZLMMYXGG5LSEA6SA43FNRTC4Y3PNYXGG5LSONXXEKBJBIQCAIBAEAQCAIDFPBRWK4DUEBWGS5DFFZCXE4TPOIQGC4ZAMU5AUIBAEAQCAIBAEAQCAIBAOBZGS3TUFAREC3RAMVZHE33SEBXWGY3VOJZGKZB2EIWCAZJOMFZGO423GBOSSCRAEAQCAIBAEAQCAIBAEBZXS4ZOMV4GS5BIFEFA====))
