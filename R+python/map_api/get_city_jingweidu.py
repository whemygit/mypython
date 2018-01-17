#!/usr/bin/env python
# -- coding: utf-8 --
import sys
import json
import requests

reload(sys)
sys.setdefaultencoding("utf-8")

add_list=["札幌","有人带","横滨","埼玉","京都","冲绳","名古屋","仙台","首都","东京","川崎","神户","大阪","广岛","福冈","首尔","京畿道","济州","光州","全罗南道","釜山","忠清北道","蔚山","庆尚南道","仁川","全罗北道","世宗","江原道","大田","庆尚北道","大邱","忠清南道","罗先","清津","金刚郡","新义州","海州","惠山","江界","元山","沙里院","平壤","咸兴","平城","开城","巴彦乌列盖省","前杭爱省","肯特省","东方省","乌布苏省","布尔干省","苏赫巴托尔省","达尔汗乌勒省","后杭爱省","扎布汗省","库苏古尔省","东戈壁省","中央省","巴彦洪果尔省","南戈壁省","鄂尔浑省","乌兰巴托","中戈壁省","科布多省","戈壁阿尔泰省","色楞格省","戈壁苏木贝尔省","碧瑶","宿雾","大雅台","马尼拉","克拉克","巴克洛德","伊洛伊洛","苏必克湾","茶胶","磅士卑","金边","暹粒","马德望","白马","柏威夏","贡布","柴桢","磅清扬","森莫诺隆","波萝勉","诗梳风","戈公","西哈努克","磅同","上丁","磅湛","桔井","菩萨省","达克茂","川圹","琅勃拉邦","沙拉湾","丰沙里","波里坎赛","沙耶武里","阿速坡","波乔","沙湾拿吉","万象","赛宋本行政特区","华潘","占巴塞","琅南塔","甘蒙","柔佛州","玻璃","彭亨","吉隆坡","吉兰丹","登嘉楼州","霹雳州","布城","森美兰","砂拉越州","吉打","雪兰莪州","槟城","纳闽","马六甲","沙巴洲","伊洛瓦底省","克钦邦","德林达依省","掸邦","马圭省","克伦邦","钦邦","实皆","若开邦","勃固省","克耶邦","仰光","内比都","曼德勒","孟邦","北榄府","洛坤府","北标府","沙敦府","沙缴府","廊磨喃蒲府","色军府","帕府","碧差汶府","华富里府","拉廊府","达叻府","乌汶府","玛哈沙拉堪府","南奔府","甘烹碧府","龙仔厝府","巴吞他尼府","攀牙府","春武里府","北大年府","武里南府","乌隆府","莫达汉府","清莱府","北碧府","帕塔亚","猜那府","宋卡府","巴真府","猜也奔府","加拉信府","程逸府","披集府","曼谷","佛丕府","红统府","素叻府","尖竹汶府","四色菊府","廊开府","清迈","乌泰他尼府","佛统府","暖武里府","甲米府","那空那育府","董里府","呵叻府","孔敬府","那空帕农府","帕尧府","叻丕府","信武里府","春蓬府","北柳府","益梭通府","黎逸府","南邦府","彭世洛府","夜功府","大城府","普吉","罗勇府","也拉府","素辇府","黎府","汶干府","北榄坡府","素攀武里府","马来奕","淡布隆","文莱－穆阿拉","斯里巴加湾","都东","北江","宁平","胡志明","莱州","岘港","高平","宣光","隆安","河内","昆嵩","芹苴","北宁","清化","谅山","海防","河江","永隆","马纳图托省","埃尔梅拉省","包考省","欧库西省","利基卡省","帝力","阿伊纳罗省","马努法伊省","劳滕省","博博纳罗省","维克克省","宏茂桥","凤山","武吉班让","东海岸","马林百列","裕廊","阿裕尼","拉丁马士","盛港西","蔡厝港","淡滨尼","义顺","波东巴西","西海岸","新加坡","丹戎巴葛","三巴旺","日惹","泗水","万隆","雅加达","棉兰","苏库尔","白沙瓦","伊斯兰堡","奎达","海得拉巴","拉瓦尔品第","卡拉奇","吉尔吉特","费萨拉巴德","拉合尔","瓜德尔港","帕罗宗","盖莱普宗","塔希央奇宗","楚卡宗","加萨宗","佩马加策尔宗","奇朗宗","通萨宗","萨姆奇宗","布姆唐宗","塔希冈宗","廷布","普那卡宗","蒙加尔宗","廷布宗","谢姆冈宗","哈阿宗","旺杜波德朗宗","萨姆德鲁琼卡尔宗","达加纳宗","伦奇宗","马累","迈门辛","库尔纳","达卡","巴里萨尔","锡尔赫特","纳拉扬甘杰","库米拉","拉杰沙希","吉大港","格尔纳利专区","塞蒂专区","纳拉亚尼专区","道拉吉里专区","蓝毗尼专区","贾纳克布尔专区","萨加玛塔专区","梅吉专区","佩里专区","戈西专区","甘达基专区","拉布蒂专区","加德满都","马哈卡利专区","巴格马蒂专区","努沃勒埃利耶","科伦坡","果阿邦","旁遮普邦","马哈拉施特拉邦","阿萨姆邦","古吉拉特邦","锡金邦","班加罗尔","曼尼普尔邦","米佐拉姆邦","查谟-克什米尔邦","恰蒂斯加尔邦","北阿坎德邦","拉贾斯坦邦","西孟加拉邦","喀拉拉邦","哈里亚纳邦","新德里","加尔各答","特里普拉邦","卡纳塔克邦","那加兰邦","比哈尔邦","贾坎德邦","泰米尔纳德邦","安得拉邦","梅加拉亚邦","奥里萨邦","北方邦","孟买","阿克托别州","东哈萨克斯坦州","阿斯塔纳","科斯塔奈州","巴甫洛达尔州","西哈萨克斯坦州","阿克莫拉州","江布尔州","卡拉干达","阿特劳州","南哈萨克斯坦州","阿拉木图","克孜勒奥尔达州","曼格斯套州","北哈萨克斯坦州","纳伦州","塔拉斯","比什凯克","贾拉拉巴德","楚河州","巴特肯","奥什州","奥什","胡占德","库利亚布","杜尚别","霍罗格","安集延州","锡尔河州","纳曼干州","吉扎克州","费尔干纳州","苏尔汉河州","纳沃伊州","塔什干","布哈拉州","塔什干州","撒马尔罕州","卡什卡达里亚州","花拉子模州","土库曼纳巴德","阿什哈巴德","达沙古兹","马雷","巴尔坎纳巴德","卡比萨省","帕克蒂卡省","塔哈尔省","洛加尔省","巴格兰省","努尔斯坦省","加兹尼省","瓦尔达克省","喀布尔","巴米扬省","朱兹詹省","尼姆鲁兹省","古尔省","帕克蒂亚省","霍斯特省","拉格曼省","巴德吉斯省","扎布尔省","法利亚布省","库纳尔省","萨尔普勒省","赫尔曼德省","楠格哈尔省","巴尔赫省","乌鲁兹甘省","赫拉特省","昆都士省","巴达赫尚省","戴孔迪省","坎大哈省","萨曼甘省","赛达","巴卜达","扎赫勒","贝鲁特","的黎波里","拉塔基亚","霍姆斯","哈塞克","大马士革","库奈特拉","代尔祖尔","拉卡","哈马","苏韦达","德拉","大马士革","伊德利卜","阿勒颇","塔尔图斯","巴士拉","拉马迪","巴格达","古巴比伦","德黑兰","胡齐斯坦省","哈马丹省","亚兹德","中央省","法尔斯省","伊拉姆省","戈勒斯坦省","阿尔达比勒省","克尔曼省","库姆省","布什尔省","克尔曼沙汗省","塞姆南省","加兹温省","霍尔木兹甘省","阿杰隆","塔菲拉","杰拉什","亚喀巴","马夫拉克","伊尔比德","安曼","扎尔卡","卡拉克","萨勒特","富查伊拉","阿治曼","阿布扎比","哈伊马角酋长国","沙迦","乌姆盖万","迪拜","巴林","麦纳麦","穆哈拉格省","赖扬","古韦里耶","梅萨伊德","乌姆锡拉勒","豪尔","多哈","乌姆巴卜","杜汉","朱迈利耶","沃克拉","费尔瓦尼耶","大穆巴拉克","科威特","哈瓦利","杰赫拉","艾哈迈迪","达曼","吉达","麦地那","利雅得","塔布克","麦加","阿什杜德","海法","耶路撒冷","贝尔谢巴","拿撒勒","佩塔提克瓦","拉姆拉","特拉维夫","耶路撒冷","加沙","尼兹瓦","马斯喀特","萨拉拉","甘贾","叶夫拉赫","纳希切万","连科兰","巴库","希尔万","纳夫塔兰","斯捷潘纳克特","舒沙","舍基","明盖恰乌尔","第比利斯","巴统","库塔伊西","帕福斯","尼科西亚","凯里尼亚","拉纳卡","法马古斯塔","利马索尔","阿依纳帕","安塔利亚","伊斯坦布尔","阿德亚曼","埃尔祖鲁姆","布尔萨","开塞利","安卡拉","安塔基亚","阿达纳","埃迪尔内","比特利斯","伊兹密尔","阿马西亚","吉雷松","迪亚巴克尔","久姆里","埃里温","荷台达","马里卜","津吉巴尔","哈杰","盖达","贝达","拉赫季","穆卡拉","焦夫","萨那","亚丁","伊卜","迈赫维特","雷克雅未克","哥本哈根","坦佩雷","赫尔辛基","图尔库","卑尔根","霍达兰","海德马克","奥斯陆","罗加兰","阿克什胡斯","特伦德拉格","奥普兰","哥德堡","乌普萨拉","斯德哥尔摩","马尔默","维尔扬迪","约赫维","纳尔瓦","沃鲁","西拉梅","帕尔努","哈普萨卢","塔尔图","库雷萨雷","拉克韦","科赫特拉-耶尔韦","瓦尔加","塔林","马杜","格罗德诺","布列斯特","戈梅利","明斯克","莫吉廖夫","维捷布斯克","圣彼得堡","哈巴罗夫斯克、伯力","下诺夫哥罗德","莫斯科","新西伯利亚","顿河畔罗斯托夫","皮亚季戈尔斯克","海参崴","叶卡捷琳堡","里加","维尔纽斯","克莱佩达","希奥利艾","考纳斯","阿利图斯","基希讷乌","本德尔","伯尔兹","基辅","塞瓦斯托波尔","萨尔茨堡","维也纳","萨尔茨堡","蒂黑","什切青","凯尔采","热舒夫","科沙林","罗兹","格丁尼亚","扎布热","奥波莱","卢布林","雷布尼克","布札希尼","格但斯克","拉多姆","奥尔什丁","瓦乌布日赫","克拉科夫","比亚韦斯托克","普沃茨克","比得哥什","格利维采","鲁达希隆斯卡","莱格尼察","弗罗茨瓦夫","琴斯托霍瓦","比托姆","埃尔布隆格","华沙","卡托维兹","汉诺威","什未林","慕尼黑","科隆","萨尔布吕肯","波茨坦","美因茨","柏林","埃尔福特","法兰克福","马格德堡","不来梅","汉堡","斯图加特","威斯巴登","杜塞尔多夫","德累斯顿","皮尔森","俄斯特拉发","布拉格","布尔诺","特里森贝格","巴札尔","伯朗肯","儒格尔","埃申","沙恩","许内勒贝格","毛伦","特里森","瓦杜兹","甘普林","巴塞尔","卢加诺","洛桑","琉森","日内瓦","卢塞恩","伯尔尼","英格堡","苏黎世","洛迦诺","圣加伦","科希策","尼特拉","布拉迪斯拉发","日利纳","久尔","塞格德","佩奇","德布勒森","米什科尔茨","布达佩斯","基尔代尔","科克","高威","都柏林","利默里克","安特卫普","布鲁塞尔","敦刻尔克","南特","尼斯","布雷斯特","波尔多","瑟堡","里摩日","戛纳","马赛","巴黎","奥尔良","图卢兹","兰斯","格勒诺布尔","里尔","第戎","佩皮尼昂","斯特拉斯堡","瓦朗斯","鲁昂","里昂","艾克斯","土伦","丹波斯","鹿特丹","海牙","马斯特里赫特","雷瓦顿","米德尔堡","莱莉","阿姆斯特丹","哈莱姆","斯瓦罗","格罗宁根","乌特勒支","阿森","安纳姆","迪基希","卢森堡","格雷文马赫","摩纳哥城","蒙特卡洛","爱丁堡","曼彻斯特","贝尔法斯特","伯明翰","伦敦","格拉斯哥","利物浦","萨兰达","斯库台","培拉特","科尔察","吉诺卡斯特州","都拉斯","地拉那","普罗夫迪夫","索非亚","布尔加斯","瓦尔纳","康斯坦察","布加勒斯特","斯科普里","库马诺沃","比托拉","普里莱普","尼什","克拉古耶瓦茨","贝尔格莱德","诺维萨德","雅典","伊拉克利翁","帕特雷","圣托里尼","塞萨洛尼基","奥林匹亚","玫瑰港","普图伊","克拉尼","布莱德","马里博尔","皮兰","科佩尔","卢布尔雅那","杜布罗夫尼克","里耶卡","扎达尔","斯普利特","奥西耶克","萨格勒布","巴尼亚卢卡","萨拉热窝","图兹拉","庞贝","威尼斯","米兰","热那亚","那不勒斯","罗马","都灵","佛罗伦萨","比萨","梵蒂冈城","基埃萨努欧瓦","塞拉瓦莱","法尔齐亚诺","圣马力诺","博尔戈·马吉欧雷","多玛尼亚诺","阿夸维瓦","科斯皮夸","斯利马","森格莱阿","瓦莱塔","巴塞罗那","帕尔马","塞维利亚","马德里","马拉加","瓦伦西亚","科尔多瓦","萨拉戈萨","波尔图","雷阿尔城","里斯本","科英布拉","莱里亚","卡尼略","马萨纳","安道尔城","恩坎普","开罗","阿斯旺","苏伊士","塞得港","亚历山大","卢克索","赫尔加达","吉萨","班加西","艾季达比耶","的黎波里","苏尔特","图卜鲁格","苏丹港","恩图曼","喀土穆","北喀土穆","阿尔及尔","奥兰","安纳巴","阿加迪尔","达尔贝达","马拉喀什","拉巴特","比塞大","突尼斯","德雷达瓦","哈勒尔","亚的斯亚贝巴","季马","马尔卡","摩加迪沙","基斯马尤","哈尔格萨","阿尔塔","吉布提","塔朱拉","蒙巴萨","内罗毕","纳库鲁","阿鲁沙","桑给巴尔","多多玛","姆万扎","姆皮吉","马萨卡","卢韦罗","穆本德","坎帕拉","基加利","布塔雷","布琼布拉","维多利亚","门德费拉","阿斯马拉","巴伦图","阿提","恩贾梅纳","马塞尼亚","奥博","班吉","布里亚","比劳","巴塔","马拉博","雅温得","马鲁阿","恩冈代雷","贝尔图阿","让蒂尔港","莫安达","利伯维尔","弗朗斯维尔","金沙萨","卡南加","卢本巴希","盆地","布昂扎","布拉柴维尔","圣多美","阿塔尔","努瓦克肖特","祖埃拉特","达喀尔","萨拉昆达","班珠尔","巴马科","库里克罗","卡伊","瓦加杜古","博罗莫","科纳克里","康康","巴法塔","比索","比绍","比翁博","阿尤恩","斯马拉","达赫拉","普拉亚","博城","马克尼","弗里敦","凯内马","蒙罗维亚","罗伯茨港","布坎南","哈泊","阿比让","亚穆苏克罗","洛美","科托努","波多诺伏","库马西","特马","阿克拉","塔马利","尼亚美","拉各斯","阿布贾","罗安达","万博","卡宾达","本格拉","恩多拉","基特韦","卢萨卡","卡布韦","哈拉雷","穆塔雷","奎鲁","布拉瓦约","奎奎","利隆圭","布兰太尔","彭巴","利欣加","马普托","太特","马翁","哈博罗内","温得和克","斯瓦科普蒙德","鲸湾港","茨瓦内","德班","布隆方丹","伊丽莎白港","开普敦","13907","约翰内斯堡","姆巴巴内","莱里贝","马塞卢","古廷","塔那那利佛","图阿马西纳","大科摩罗岛","莫罗尼","罗斯希尔","苏亚克","巴姆布斯","路易港","柏斯","霍巴特","佩斯","堪培拉","爱丽丝泉","达尔文","墨尔本","凯恩斯","阿德莱德","布里斯班","悉尼","达尼丁","惠灵顿","基督城","奥克兰","莫尔斯比港","霍尼亚拉","维拉港","诺索普","帕利基尔","维诺","科洛尼亚","马朱罗","马卡拉尔","科罗尔","梅莱凯奥克","亚伦","塔拉瓦","富纳富提","阿皮亚","楠迪","苏瓦","拉米","劳托卡","努库阿洛法","阿瓦鲁阿","努美阿","阿洛菲","芝加哥","林肯","达拉斯","洛利","哈立斯堡","蒙特利埃","凤凰城","塔拉哈希","新奥尔良","华盛顿","杰克逊县","匹兹堡","亚特兰大","奥尔巴尼","奥克拉荷马","奥斯汀","夏延","丹佛","第蒙","费城","康科德","哥伦布","普罗维登斯","西雅图","小石城","波易士","亚纳波里","洛杉矶","赫勒那","迈阿密","罗切斯特","波特兰","盐湖城","朱诺","多佛","巴顿鲁治","底特律","波士顿","圣菲","克利夫兰","纳什维尔","麦迪逊","长滩","印第安纳波里","休斯敦","卡逊城","俾斯麦","巴尔的摩","列治文","钱德勒","檀香山","奧古斯塔","纽约","杰斐逊","水牛城","塞伦","圣安东尼","蒙哥马利","拉斯维加斯","哈特佛特","托派卡","兰辛","旧金山","特伦顿","辛辛那提","皮尔","查尔斯顿","萨克拉曼多","春田","蒙特利尔","汉密尔顿","卡尔加里","爱民顿","多伦多","温尼伯","温哥华","渥太华","滑铁卢","埃德蒙顿","瓜达拉哈拉","莱昂","墨西哥城","蒙特雷","普埃布拉","巴里奥斯港","危地马拉城","奥兰治沃克","贝尔莫潘","圣萨尔瓦多","乌苏卢坦","圣维森特","胡蒂卡尔帕","特古西加尔巴","希诺特佩","马那瓜","马萨亚","布卢菲尔兹","蓬塔雷纳斯","圣何塞","利蒙","戴维","巴拿马城","科隆","大巴哈马岛","拿骚","圣地亚哥","哈瓦那","圣克拉拉","蒙坦戈贝","金斯敦","西班牙镇","和平港","太子港","戈纳伊夫","圣多明各","拉罗马纳","拉贝加","圣玛丽","圣约翰","圣飞利浦","圣保罗","圣彼得","圣乔治","安提瓜岛","巴斯特尔","罗索","韦斯利","金斯敦","圣乔治","布里奇顿","西班牙港","圣乔治","圣安德鲁","圣胡安","罗德城","马拉开波","拉瓜伊拉","加拉加斯","巴伦西亚","乔治敦","新尼克里","帕拉马里博","基多","昆卡","利马","特鲁希略州","库斯科","拉巴斯","圣克鲁斯","苏克雷","巴西利亚","伊瓜苏","里约热内卢","累西腓","圣保罗","马瑙斯","瓦尔帕莱索","伊基克","蓬塔阿雷纳斯","康塞普西翁","圣地亚哥","罗萨里奥","科尔多瓦","布宜诺斯艾利斯","恩卡纳西翁","亚松森","蒙得维的亚","萨尔托","波哥大","朱巴","NULL","景德镇","宜春","抚州","新余","萍乡","赣州","樟树","南昌","贵溪","鹰潭","吉安","上饶","南昌县","九江","聊城","昌邑","枣庄","肥城","滨州","胶州","恒台县","青州","泰安","青岛","烟台","招远","莱西","莱芜","威海","茌平","潍坊","菏泽","德州","诸城","广饶","平阴","即墨","济宁","东营","淄博","桓台","日照","济南","新泰","莱州","禹城","荣成","邹城","龙口","临沂","常德","长沙县","湘潭","张家界","永州","邵阳","岳阳","怀化","长沙","株洲","郴州","衡阳","湘西","益阳","娄底","惠州","梅州","深圳","韶关","潮州","广州","江门","珠海","汕头","湛江","揭阳","肇庆","清远","佛山","东莞","四会","河源","中山","阳江","汕尾","云浮","茂名","开封","焦作","巩义","洛阳","濮阳","永城","郑州","鹤壁","平顶山","信阳","新郑","长葛","三门峡","许昌","荥阳","新乡","济源","禹州","漯河","南阳","驻马店","安阳","商丘","周口","鄂尔多斯","兴安盟","乌海","锡林郭勒","通辽","托克托","阿拉善盟","赤峰","呼和浩特","乌兰察布","呼伦贝尔","巴彦淖尔","包头","高雄","桃园","台南","新北","台中","台北","临沧","楚雄","保山","昭通","安宁","玉溪","大理","丽江","迪庆","西双版纳","文山","曲靖","德宏","昆明","红河","怒江","普洱","海西","果洛","玉树","海北","海南藏族","西宁","海东","黄南","乐清","慈溪","桐乡","德清","宁波","绍兴","东阳","衢州","丽水","温岭","台州","义乌","金华","海宁","嘉兴","平湖","杭州","湖州","嘉善","诸暨","长兴","温州","永康","瑞安","玉环","象山","舟山","本溪","大石桥","辽阳","海城","丹东","锦州","瓦房店","盘锦","沈阳","阜新","抚顺","朝阳","庄河","葫芦岛","大连","营口","铁岭","鞍山","辽源","绿园","四平","经济技术开发区","净月旅游开发区","南关","吉林","农安","延边朝鲜族自治州","九台","白城","宽城","德惠","长春","延吉","榆树","松原","白山","双阳","二道","汽车产业开发区","朝阳区","高新技术产业开发区","双鸭山","大兴安岭","哈尔滨","七台河","鹤岗","安达","齐齐哈尔","绥化","鸡西","佳木斯","大庆","牡丹江","伊春","黑河","凉山","雅安","甘孜","攀枝花","德阳","自贡","绵阳","广元","泸州","宜宾","遂宁","内江","巴中","成都","眉山","阿坝","南充","西昌","资阳","广安","乐山","达州","NULL","铜仁","安顺","贵阳","盘州","测试市","黔西","六盘水","毕节","仁怀","遵义","黔南","测试","黔东","NULL","那曲","山南","拉萨","日喀则","昌都","林芝","阿里","昌吉","乌鲁木齐","库尔勒","唐山","衡水","万泉","邢台","石家庄","香河","阳原","保定","任丘","武安","沽源","宣化","承德","定州","尚义","张家口","沧州","邯郸","秦皇岛","廊坊","雄安","惠安","泉州","宁德","三明","南安","南平","厦门","安溪","莆田","漳州","晋江","福清","福州","龙岩","泰州","如皋","建湖","启东","高邮","扬中","太仓","如东","丹阳","连云港","江阴","沛县","东台","新沂","扬州","溧阳","句容","淮安","常熟","徐州","宜兴","南通","昆山","常州","邳州","仪征","盐城","苏州","南京","无锡","宿迁","海安","海门","镇江","张家港","三亚","定安","陵水","五指山","临高县","西沙群岛","文昌","昌江","屯昌","保亭","琼海","南沙群岛","万宁","乐东","东方","海口","澄迈","琼中","儋州","中沙群岛的岛礁及其海域","白沙","康乐","永靖","银川","吴忠","和政","广河","临夏县","中卫","东乡","灵武","临夏","积石山","张掖","白银","定西","嘉峪关","甘南","金昌","陇南","庆阳","兰州","天水","武威","平凉","酒泉","百色","崇左","桂林","玉林","北海","南宁","来宾","贵港","柳州","防城港","阳朔","河池","钦州","梧州","贺州","天门","宜昌","武汉","随州","仙桃","荆门","黄冈","宜都","襄阳","荆州","神农架","潜江","咸宁","十堰","恩施","大冶","鄂州","孝感","黄石","澳门","香港","肥西","肥东","黄山","天长","合肥","阜阳","宿州","宁国","马鞍山","安庆","池州","当涂","滁州","芜湖","铜陵","淮南","宣城","淮北","蚌埠","亳州","六安","NULL","上海","北京","重庆","天津","太原","晋城","大同","朔州","阳泉","长治","晋中","运城","吕梁","孝义","临汾","忻州","铜川","神木","商洛","宝鸡","西安","安康","府谷","咸阳","渭南","汉中","榆林","延安"]
# add_list=['北京','上海']
def getlnglat():
    url='http://api.map.baidu.com/geocoder/v2/'
    output='json'
    ak='Qk77GopeGV7dPCPAAHpLHG0sl87pGbcV'
    # add='北京市海淀区上地十街10号'

    for i in add_list:
        uri=url+'?'+'address='+i+'&output=' + output + '&ak=' + ak
        resp=requests.get(uri)
        res=resp.text
        temp=json.loads(res)
        try:
            yield i,temp['result']['location']
        except:
            print i


if __name__ == '__main__':
    for i in add_list:
        print i
    # with open('city_lng_lat','w') as fw:
    #     for i,j in getlnglat():
    #         fw.write(i+','+str(j['lng'])+','+str(j['lat'])+'\n')