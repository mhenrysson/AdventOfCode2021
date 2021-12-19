import math


def main():
    print("First test: ", first(get_test_input()))
    print("First real: ", first(get_input()))
    print("Second test: ", second(get_test_input()))
    print("Second real: ", second(get_input()))


def first(inputs: str):
    points, _ = get_points(inputs)
    return len(points)


def second(inputs: str):
    _, scanners = get_points(inputs)
    longest = 0
    for p1 in scanners:
        for p2 in scanners:
            dist = sum([abs(scanners[p1][a] - scanners[p2][a]) for a in range(3)])
            longest = max(dist, longest)
    return longest


def get_points(inputs):
    scanners = inputs.split("\n\n")
    beacons = [s.splitlines()[1:] for s in scanners]
    point_vectors = []
    for b in beacons:
        for j in range(len(b)):
            b[j] = [int(v) for v in b[j].split(',')]
        point_vectors.append(generate_point_vectors(b))
    aligned = set([0])
    unaligned = set(range(1, len(beacons)))
    scanners = {0: [0, 0, 0]}
    while unaligned:
        realigned = set()
        for i in unaligned:
            for j in aligned:
                hits = [k for k in point_vectors[i] if k in point_vectors[j]]
                if len(hits) >= 66:  # 1+2+3+..+11
                    hithit = None
                    for hit in hits:
                        (p1, p2), (q1, q2) = point_vectors[i][hit], point_vectors[j][hit]
                        for h in hits:
                            if h != hit:
                                (r1, r2), (s1, s2) = point_vectors[i][h], point_vectors[j][h]
                                if (p1 == r1 and q1 == s1) or (p2 == r2 and q2 == s2):
                                    hithit = hit
                                    break
                                if (p1 == r2 and q2 == s1) or (q2 == r1 and q1 == s2):
                                    point_vectors[i][hit] = (point_vectors[i][hit][1], point_vectors[i][hit][0])
                                    hithit = hit
                                    break
                        if hithit:
                            break
                    v = [[beacons[n][point_vectors[n][hithit][0]][k] - beacons[n][point_vectors[n][hithit][1]][k] for k
                          in range(3)] for n in [i, j]]
                    rot = [[int(math.copysign(1, (v[0][d])) * math.copysign(1, (v[1][e])))
                            if abs((v[0][d])) == abs((v[1][e])) else 0
                            for d in range(3)] for e in range(3)]
                    v0 = [sum([rot[n][m] * beacons[i][point_vectors[i][hithit][0]][m] for m in range(3)]) for n in
                          range(3)]
                    move = [beacons[j][point_vectors[j][hithit][0]][n] - v0[n] for n in range(3)]
                    scanners[i] = move
                    for nn in range(len(beacons[i])):
                        beacons[i][nn] = [sum([rot[n][m] * beacons[i][nn][m] for m in range(3)]) + move[n] for n in
                                          range(3)]
                    point_vectors[i] = generate_point_vectors(beacons[i])
                    realigned.add(i)
                    break
        for i in realigned:
            unaligned.remove(i)
            aligned.add(i)
    points = list(set([tuple(p) for b in beacons for p in b]))
    return points, scanners


def generate_point_vectors(beacons):
    pv = {}
    for i in range(len(beacons)):
        for j in range(i):
            ls = [abs(beacons[i][k] - beacons[j][k]) for k in range(3)]
            ls.sort()
            pv[tuple(ls)] = (i, j)
    return pv


def get_test_input():
    return """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""


def get_input():
    return """--- scanner 0 ---
343,-529,464
562,-568,-779
545,-448,-791
717,-502,-775
-482,-762,-507
753,757,-789
-574,-799,339
510,688,511
15,78,-83
-556,-789,506
326,-589,494
-495,-826,-357
-144,-12,3
359,-464,436
-511,-799,-562
-566,447,-909
757,654,-914
-562,587,312
-490,568,298
481,747,633
-763,386,-919
-586,-723,310
520,831,581
-672,427,-808
735,709,-786
-615,622,336

--- scanner 1 ---
496,-531,-490
-559,-887,-819
390,-749,652
-558,568,-690
521,508,-470
-830,-337,543
750,351,440
488,-331,-501
88,-80,94
418,-454,-441
-626,624,-807
371,-759,487
-665,468,-746
-537,-768,-737
-800,-401,664
-515,387,712
517,732,-490
-536,514,615
-776,-338,751
-584,-887,-622
381,-765,621
739,307,659
-526,437,520
513,613,-534
702,360,583
-76,81,105

--- scanner 2 ---
-347,490,818
-668,748,-588
-656,749,-527
-712,-614,408
-567,722,-531
-425,560,784
-514,-537,-659
521,493,789
-472,-489,-804
481,-816,779
57,-118,51
664,365,-303
-825,-498,426
450,-773,914
816,-640,-698
799,-680,-727
-409,503,783
697,397,-502
685,407,802
-426,-537,-632
-805,-505,485
651,427,-464
800,-763,-797
457,-706,894
565,427,891

--- scanner 3 ---
-774,795,800
467,812,-297
-563,-601,571
-491,-307,-280
-612,-337,-344
-726,829,774
-468,-611,494
428,736,886
674,-553,-830
586,673,-277
859,-511,681
798,-472,525
-660,-622,444
423,684,-286
474,604,822
-618,844,-619
-650,794,-759
-699,-361,-281
789,-600,-711
871,-578,-830
-18,48,72
334,659,802
742,-579,625
-639,831,802
-610,941,-781

--- scanner 4 ---
-339,642,664
826,518,-846
704,-836,674
851,412,-792
-714,-385,808
-803,-343,729
655,897,382
-786,548,-583
783,-864,666
49,39,25
-724,483,-468
692,-816,-890
-337,761,788
-32,-79,-123
722,-748,751
-761,459,-477
648,-834,-848
-749,-379,599
-400,-396,-449
-340,525,741
-495,-414,-451
710,757,362
932,468,-870
578,803,298
758,-845,-832
-579,-410,-392

--- scanner 5 ---
861,802,355
-721,-597,579
-599,-382,-788
131,-64,-128
461,509,-411
513,551,-440
-575,790,357
-670,808,355
-321,825,-693
-267,861,-823
-637,-636,631
-491,794,298
574,-758,434
-544,-360,-916
874,909,413
-647,-364,-791
699,-791,492
78,85,24
-356,819,-902
554,560,-484
961,891,328
639,-774,462
-578,-607,509
678,-555,-781
558,-572,-793
612,-400,-777

--- scanner 6 ---
591,-720,-461
-685,-551,-599
698,448,529
437,577,-451
-800,358,-509
-769,-603,-638
-76,-63,-88
341,460,-454
-791,636,506
785,-874,468
526,-748,-477
714,411,582
851,-678,438
743,355,448
-806,474,-369
-560,-848,497
-506,-886,372
-735,364,-407
861,-845,456
344,598,-499
50,71,13
-525,-872,444
-838,572,578
-626,-673,-628
-807,681,737
651,-690,-444

--- scanner 7 ---
-716,674,326
740,-531,-518
573,-477,-462
-359,-557,554
856,748,-838
951,-595,466
410,725,486
-654,575,-868
-591,-337,-795
857,631,-761
-654,661,487
-332,-646,550
-333,-658,611
-17,-25,8
582,-584,-499
472,790,371
915,-522,536
83,84,-129
-674,695,-779
-578,-399,-760
859,512,-885
-588,531,-766
-521,-415,-761
831,-611,468
435,814,380
-684,707,525

--- scanner 8 ---
874,-748,440
-470,-647,434
-329,468,819
-358,-451,-704
876,-846,-692
26,-39,130
-526,-715,551
-633,395,-802
962,-813,432
879,352,580
800,-763,434
865,420,-783
-265,600,865
-362,-432,-574
825,327,474
897,-801,-761
-641,474,-774
881,530,-772
-507,-401,-657
923,486,-754
-626,-608,495
-349,523,959
132,-170,25
912,-882,-671
903,246,530
-718,456,-686

--- scanner 9 ---
220,789,846
699,886,-436
296,-279,-648
-450,765,481
544,-364,461
-796,-404,-390
-805,-531,-328
253,-291,-773
2,54,91
-178,146,153
624,-400,479
730,892,-415
-492,674,644
246,679,690
248,778,755
596,-281,532
-542,645,-686
-797,-481,-400
674,838,-446
-415,672,-640
-528,699,495
-412,756,-641
-689,-244,881
-664,-334,773
249,-410,-662
-714,-308,725

--- scanner 10 ---
-743,-577,-906
0,-10,75
-706,500,-637
589,645,-798
-672,-467,-868
654,617,-814
407,-701,-776
-528,-687,489
-563,570,-647
404,-563,-821
976,751,851
889,666,869
-655,724,768
714,587,-831
876,724,762
113,-185,-92
-560,722,750
958,-929,624
-737,-461,-766
500,-680,-824
-504,-590,394
-622,448,-676
767,-932,673
-476,781,754
874,-774,647
-530,-626,498

--- scanner 11 ---
-610,758,711
-39,5,29
441,517,-527
639,-532,-302
644,-802,891
-814,743,-318
-575,-787,-423
346,614,-551
450,578,-525
-674,763,894
-555,-661,468
-954,627,-312
-111,-180,95
-484,-647,-467
746,-651,901
-618,710,893
-477,-521,466
-558,-536,436
582,-726,933
657,-421,-364
542,-410,-307
-916,737,-383
304,507,384
376,396,406
-450,-769,-479
272,295,365

--- scanner 12 ---
-520,574,-422
-459,-728,-692
-515,593,-608
773,449,663
-278,513,533
13,-95,143
-352,-873,427
-366,600,593
-260,558,665
509,-901,-743
-505,-766,-662
-376,-882,464
-482,471,-519
624,597,-741
-441,-767,402
402,-843,-756
517,-958,609
647,752,-825
877,413,637
598,755,-634
-492,-927,-724
503,-901,788
420,-928,-843
184,4,25
521,-899,693
782,510,661

--- scanner 13 ---
699,-519,854
-509,-456,834
812,326,-413
719,399,-464
-589,-379,796
399,-498,-813
760,355,-455
-776,364,678
715,708,668
-685,-728,-363
-698,-750,-503
661,692,496
-715,-898,-404
312,-413,-795
574,-577,887
595,696,651
-717,331,670
412,-440,-706
-757,334,-269
-837,331,-289
13,-62,64
-492,-413,889
-782,271,-246
634,-547,870
-659,309,778

--- scanner 14 ---
-591,-463,592
963,496,-448
-535,331,-928
816,-521,-678
797,-837,721
873,650,-474
549,693,771
551,555,683
-524,423,-991
84,48,-3
-473,465,214
-457,467,334
498,449,775
905,-625,-586
94,-93,-183
733,-803,532
-336,-482,-550
-537,-519,425
-656,386,-874
794,511,-474
-546,535,250
745,-876,534
-471,-480,-514
794,-661,-551
-384,-508,-516
-484,-500,583

--- scanner 15 ---
769,-544,-399
346,417,-553
3,13,-132
683,-511,725
-164,-157,-141
-118,-88,54
-426,315,626
511,667,832
-819,-749,-462
303,387,-559
607,-594,-401
462,338,-505
-779,437,-738
-432,260,640
719,-475,704
-499,325,711
-555,-925,607
-719,-642,-518
704,-556,794
-555,433,-718
681,-609,-407
-663,-710,-401
489,696,674
426,714,846
-674,429,-674
-700,-956,690
-551,-906,737

--- scanner 16 ---
-425,-563,384
-365,353,319
-645,450,-524
-403,-671,442
-425,396,264
592,-460,-991
665,-528,-905
853,417,-747
28,120,-178
473,-571,-943
319,-782,609
362,-727,592
-458,-571,325
285,-689,512
-89,39,-25
758,485,-676
-481,-688,-578
634,470,416
-384,-784,-485
669,475,-804
-726,549,-448
-457,-798,-509
804,511,386
656,610,403
-603,665,-497
-428,376,344

--- scanner 17 ---
-116,49,-25
-654,389,-451
723,-662,336
-554,334,-568
687,-742,354
-537,412,452
-498,-431,-718
-441,315,359
-427,388,383
-765,-661,865
-662,356,-510
-654,-542,817
606,679,-525
806,-714,407
-443,-388,-735
677,-367,-787
753,546,648
-697,-734,779
683,678,-515
843,571,756
-536,-354,-638
27,-99,-125
796,-371,-898
556,687,-453
779,596,600
808,-414,-773

--- scanner 18 ---
-327,-658,-724
785,-570,464
64,89,-38
867,909,-604
596,767,758
676,729,835
855,-700,-579
971,899,-592
966,906,-562
-225,-862,801
-794,765,-651
802,-471,316
-487,820,637
-547,803,667
-243,-635,-879
-701,813,-630
-325,-773,774
-312,-880,716
579,822,801
931,-751,-621
-434,-684,-882
815,-572,-619
-797,810,-513
772,-430,486
-612,787,695

--- scanner 19 ---
672,618,495
344,-597,-447
-888,-375,-736
364,-824,666
722,629,687
-660,595,560
364,-652,-307
595,608,590
641,479,-771
-810,-456,-792
-859,619,-826
-864,-481,-686
366,-788,801
280,-729,-401
-447,-410,602
-698,506,593
541,586,-715
-22,15,30
-502,-464,481
-947,684,-834
-539,-347,613
392,-822,753
-794,561,510
-785,634,-832
485,518,-832

--- scanner 20 ---
705,639,816
529,735,-475
-416,-396,746
-732,386,464
446,-421,-321
541,725,829
511,-359,-436
-422,-431,955
-350,886,-275
-681,479,537
-110,-90,109
562,767,-276
605,-806,811
-439,786,-302
34,17,-11
575,705,-437
724,-808,935
488,-805,888
-447,-566,-245
-451,-650,-304
-690,438,493
-332,799,-360
422,-384,-330
661,705,918
-433,-745,-302
-380,-342,876

--- scanner 21 ---
-473,-470,-913
-348,-672,653
-294,-748,489
-490,-444,-862
739,870,826
-395,765,347
-443,491,-594
680,835,-831
-314,497,-612
-619,-405,-899
722,759,-780
-441,-656,466
671,-797,733
-556,449,-620
-397,832,279
682,719,-652
-355,674,319
422,-339,-715
650,-890,685
419,-530,-764
103,-70,1
788,-893,730
697,771,829
709,875,819
577,-423,-738

--- scanner 22 ---
792,-745,698
873,713,548
57,101,91
752,-469,-488
692,-689,591
-330,-648,-438
647,-533,-480
-547,619,671
823,521,559
-472,579,-549
-509,586,582
953,660,-706
909,441,-717
-796,-808,493
900,584,-669
-458,603,-405
-708,-800,558
-643,536,616
-373,-654,-468
-489,-702,-389
746,616,569
-634,-806,543
636,-806,659
528,-489,-484
-376,688,-521

--- scanner 23 ---
112,40,-75
358,-728,-881
-663,631,431
717,644,-589
711,584,519
809,-551,372
-713,636,592
920,-460,331
-633,539,-516
-514,504,-387
508,-741,-817
910,-657,392
-311,-661,532
-309,-637,-778
687,573,-596
-338,-649,-854
885,574,-630
-505,-667,-844
-297,-733,513
722,507,399
-627,412,-473
-3,80,78
563,-712,-854
-335,-608,567
-604,609,452
744,596,486

--- scanner 24 ---
-522,-399,729
-540,734,581
495,401,519
-500,-590,-519
-520,-363,594
-559,576,528
-879,460,-751
291,-777,530
654,-731,-864
708,-706,-758
346,-723,409
445,906,-728
383,-840,541
-926,457,-515
-548,-365,681
-520,-535,-379
14,9,1
-503,743,474
427,485,608
330,844,-793
732,-812,-808
425,365,592
339,881,-817
-158,130,-33
-802,459,-634
-436,-458,-473

--- scanner 25 ---
447,601,421
653,-348,-776
505,440,-472
-568,618,531
-359,612,455
-709,653,-664
-7,144,-123
-464,-810,-794
519,437,-547
24,-7,19
494,-827,325
-451,556,579
512,434,-622
-786,-396,618
613,-326,-923
424,694,443
615,-763,355
-868,-277,596
445,461,420
-759,633,-860
-671,-277,571
-420,-821,-666
702,-826,379
-583,-830,-655
621,-488,-826
-639,699,-778

--- scanner 26 ---
-595,508,564
552,330,-825
609,-510,797
667,341,-768
784,540,750
649,452,-830
-474,567,-665
-814,-583,330
460,-658,-607
-440,689,-653
635,-352,690
-804,-823,-814
451,-597,-605
8,88,-69
733,557,776
-618,361,472
-944,-707,-820
356,-694,-581
-906,-817,-749
-862,-604,423
-782,415,548
-859,-721,327
-128,-43,-32
586,-355,881
770,686,815
-565,707,-709

--- scanner 27 ---
-668,457,-530
-690,-336,620
-392,-403,-533
233,599,429
746,586,-412
651,-472,-845
389,-714,831
-685,402,666
30,-87,115
-543,361,-494
-776,360,829
-530,506,-503
270,-686,778
353,-634,849
653,474,-474
-710,438,815
-789,-338,555
-429,-476,-605
-374,-507,-469
323,574,537
-800,-310,464
-111,-2,3
740,-480,-658
297,624,585
602,632,-409
712,-498,-854

--- scanner 28 ---
633,-520,-710
9,91,-13
-762,828,-897
726,-665,426
-535,311,500
615,-630,-785
-784,-637,-574
-770,-725,-633
-790,-597,603
-623,828,-818
370,752,312
676,-654,618
599,-644,523
-166,100,-161
-694,-542,520
549,751,-818
-608,854,-987
-656,-631,553
368,788,447
-726,-544,-656
531,-619,-688
409,624,-840
-443,374,511
-498,428,632
513,716,-929
-71,-71,-74
396,786,360

--- scanner 29 ---
675,-576,799
-658,284,770
-698,431,748
-104,61,25
-674,-703,-793
675,-578,829
419,413,286
422,-426,-407
286,566,-813
538,552,266
-897,-769,640
-822,430,-811
642,-616,659
-621,-545,-774
375,541,275
54,31,-125
-567,-712,-830
426,621,-833
-783,-740,598
-842,-783,459
658,-429,-454
-666,381,608
380,489,-897
-774,396,-785
-687,394,-813
541,-428,-531

--- scanner 30 ---
-606,844,719
501,414,422
814,-595,-760
-563,-317,576
768,799,-397
-103,-4,171
743,-869,460
877,-606,-668
791,-849,380
743,693,-343
-587,-316,605
-678,738,761
760,-474,-705
-328,-657,-626
849,743,-319
355,299,401
533,309,458
-807,728,-721
-738,826,674
-869,663,-606
-481,-328,548
718,-684,432
-844,752,-712
-448,-673,-624
21,-57,15
-364,-584,-556"""


if __name__ == '__main__':
    main()
