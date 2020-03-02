#!/usr/bin/env python
import rospy 
import numpy as np
import pandas as pd
from sensor_msgs.msg import LaserScan

inf=99999

def preprocessing(ranges,theta):
    if theta>=0 and theta<45:
        left=np.min(ranges[45-theta:135-theta])
        right=np.min(ranges[225-theta:315-theta])
    
    elif theta>=45 and theta<135:
        left1=np.min(ranges[405-theta:])
        left2=np.min(ranges[:135-theta])
        left=np.min([left1,left2])
        right=np.min(ranges[225-theta:315-theta])
    elif theta>=135 and theta<215:
        left=np.min(ranges[405-theta:495-theta])
        right=np.min(ranges[225-theta:315-theta])
    elif theta>=215 and theta<315:
        left=np.min(ranges[405-theta:495-theta])
        right1=np.min(ranges[585-theta:])
        right2=np.min(ranges[:315-theta])
        right=np.min([right1,right2])
    else:
        left=np.min(ranges[405-theta:495-theta])
        right=np.min(ranges[585-theta:675-theta])

    return left,right

def callback(scan):
    ranges=scan.ranges
    #print(scan)
    ranges=np.array(ranges)
    print(ranges.shape)
    left,right=preprocessing(ranges,0)
    print(left,right)

def fcallback(scan):
    pass
scan_sub=rospy.Subscriber('/scan',LaserScan,fcallback)

def main():
    rospy.init_node('range',anonymous=True)
    scan_sub=rospy.Subscriber('/scan',LaserScan,callback)
    #scan_sub.unregister()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "shutting down"
    #scan=[2.1398766040802, 2.183053493499756, 2.2498865127563477, 2.2920379638671875, 2.37719464302063, 2.4384000301361084, 2.5300896167755127, 2.603621244430542, 2.706026792526245, 2.78368878364563, 2.9284214973449707, 3.026472568511963, 3.132024049758911, 3.282510757446289, 3.4400923252105713, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 3.2923009395599365, 2.9724254608154297, 2.6951074600219727, 2.4704549312591553, 2.2790768146514893, 2.1098594665527344, 1.9634407758712769, 1.8310388326644897, 1.7378019094467163, 1.6493992805480957, 1.5366897583007812, 1.4678055047988892, 1.4152501821517944, 1.3522813320159912, 1.297955870628357, 1.2465767860412598, 1.1994199752807617, 1.14863121509552, 1.124190092086792, 1.0680060386657715, 1.0394619703292847, 1.025942325592041, 0.9823716878890991, 0.9493356347084045, 0.9289017915725708, 0.911404550075531, 0.861850917339325, 0.8532099723815918, 0.8384931087493896, 0.8111453056335449, 0.8031547665596008, 0.7790350317955017, 0.7737982869148254, 0.7495595216751099, 0.7249558568000793, 0.7277526259422302, 0.7230242490768433, 0.6970884799957275, 0.6884129643440247, 0.681270956993103, 0.6646636724472046, 0.6599351763725281, 0.6389597654342651, 0.6283758282661438, 0.634648859500885, 0.6142013072967529, 0.6261317729949951, 0.6095007061958313, 0.6139408349990845, 0.5928573608398438, 0.599662184715271, 0.5741615295410156, 0.5753737092018127, 0.5757554769515991, 0.5640871524810791, 0.5715697407722473, 0.5551857352256775, 0.5385550260543823, 0.5482628345489502, 0.5284650921821594, 0.5267614126205444, 0.5307731032371521, 0.5348688364028931, 0.5161746144294739, 0.512956976890564, 0.5196658968925476, 0.5160576105117798, 0.5147382616996765, 0.5094606876373291, 0.5332629680633545, 0.517556369304657, 0.5124265551567078, 0.5046124458312988, 0.5019734501838684, 0.49394914507865906, 0.5183172225952148, 0.4988955557346344, 0.5028601884841919, 0.4984968602657318, 0.4958666265010834, 0.4972885549068451, 0.5069876313209534, 0.48780035972595215, 0.49479037523269653, 0.4977462589740753, 0.4901432991027832, 0.4943191707134247, 0.5020068883895874, 0.4946747124195099, 0.5124657154083252, 0.5104140043258667, 0.5028466582298279, 0.5018986463546753, 0.5255803465843201, 0.5010643601417542, 0.527937650680542, 0.505728006362915, 0.514535665512085, 0.5190155506134033, 0.5122058391571045, 0.5457748770713806, 0.53709876537323, 0.5321071147918701, 0.534197211265564, 0.5347087979316711, 0.5530329346656799, 0.5667877197265625, 0.5740984678268433, 0.5645476579666138, 0.5735435485839844, 0.5760881304740906, 0.5767607092857361, 0.58757483959198, 0.5912074446678162, 0.5773093700408936, 0.591452419757843, 0.6133223176002502, 0.6289997100830078, 0.6165090203285217, 0.6303918361663818, 0.6513873934745789, 0.6593849658966064, 0.6593078374862671, 0.692474901676178, 0.6784865856170654, 0.6996451020240784, 0.6978909373283386, 0.7281008958816528, 0.7463399767875671, 0.7596834897994995, 0.7594661116600037, 0.7869939208030701, 0.7924354076385498, 0.8126518726348877, 0.8288282155990601, 0.8563929796218872, 0.8790850043296814, 0.904106855392456, 0.9111158847808838, 0.9411705732345581, 0.9638162851333618, 1.0203856229782104, 1.0491713285446167, 1.0606906414031982, 1.1143624782562256, 1.1451607942581177, 1.190373182296753, 1.2486495971679688, 1.2779273986816406, 1.3527010679244995, 1.4074746370315552, 1.3976472616195679, 1.3907533884048462, 1.3873904943466187, 1.3881840705871582, 1.367305040359497, 1.3539841175079346, 1.3597056865692139, 1.3448586463928223, 1.341741919517517, 1.3352056741714478, 1.3435988426208496, 1.331989049911499, 1.3198102712631226, 1.3228133916854858, 1.3143607378005981, 1.3319212198257446, 1.3311817646026611, 1.2893800735473633, 1.315981388092041, 1.3192222118377686, 1.3099092245101929, 1.3197721242904663, 1.3100789785385132, 1.3190094232559204, 1.3344558477401733, 1.3003673553466797, 1.3377704620361328, 1.3342044353485107, 1.3299838304519653, 1.3477177619934082, 1.332170844078064, 1.332425594329834, 1.3449556827545166, 1.3303942680358887, 1.3603659868240356, 1.355437994003296, 1.3648651838302612, 1.3677719831466675, 1.3929780721664429, 1.3891533613204956, 1.406653881072998, 1.4085776805877686, 1.4076780080795288, 1.4361094236373901, 1.4336533546447754, 1.4427679777145386, 1.4600343704223633, 1.4695426225662231, 1.4853068590164185, 1.5168442726135254, 1.513486623764038, 1.5453284978866577, 1.5541396141052246, 1.5908050537109375, 1.5685616731643677, 1.6020252704620361, 1.6379209756851196, 1.6448034048080444, 1.6878117322921753, 1.686564564704895, 1.7048283815383911, 1.7517814636230469, 1.7750500440597534, 1.7520042657852173, 1.710963487625122, 1.6726467609405518, 1.6566452980041504, 1.6200162172317505, 1.6153088808059692, 1.5819339752197266, 1.5633673667907715, 1.534515142440796, 1.4958831071853638, 1.506272315979004, 1.4783114194869995, 1.455260992050171, 1.4407541751861572, 1.4262304306030273, 1.4060084819793701, 1.4064698219299316, 1.3920090198516846, 1.3701467514038086, 1.372902750968933, 1.3458253145217896, 1.3395185470581055, 1.3267223834991455, 1.308465838432312, 1.3046133518218994, 1.291405200958252, 1.282047152519226, 1.2989708185195923, 1.2783546447753906, 1.265971064567566, 1.2540005445480347, 1.2742128372192383, 1.228843331336975, 1.2427250146865845, 1.2316620349884033, 1.2193143367767334, 1.2275995016098022, 1.2042920589447021, 1.2119213342666626, 1.213340163230896, 1.19576895236969, 1.1874467134475708, 1.1937015056610107, 1.2154408693313599, 1.1961028575897217, 1.2169382572174072, 1.197253704071045, 1.2077800035476685, 1.210802674293518, 1.21146821975708, 1.215436339378357, 1.2151076793670654, 1.1994547843933105, 1.2125061750411987, 1.215028166770935, 1.2177389860153198, 1.2251888513565063, 1.2024857997894287, 1.2400275468826294, 1.2122690677642822, 1.2319247722625732, 1.2468141317367554, 1.2425204515457153, 1.2229962348937988, 1.2669296264648438, 1.278110146522522, 1.2761962413787842, 1.2805663347244263, 1.2938427925109863, 1.2944303750991821, 1.323831558227539, 1.3056118488311768, 1.3239043951034546, 1.3637988567352295, 1.3681225776672363, 1.3654308319091797, 1.3794407844543457, 1.3955131769180298, 1.4050688743591309, 1.4231014251708984, 1.4471758604049683, 1.4530260562896729, 1.4763046503067017, 1.511998176574707, 1.520582914352417, 1.5337574481964111, 1.5499815940856934, 1.5714555978775024, 1.5875697135925293, 1.6250832080841064, 1.6435619592666626, 1.6951298713684082, 1.7233868837356567, 1.7651525735855103, 1.7733575105667114, 1.8174850940704346, 1.8453657627105713, 1.8969305753707886, 1.9369672536849976, 1.9828194379806519, 2.0051486492156982, 2.081026315689087, 2.12443470954895]
    
    
if __name__ == "__main__":
    main()

    