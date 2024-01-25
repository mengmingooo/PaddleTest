#!/bin/env python3
# -*- coding: utf-8 -*-
# @author DDDivano
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python


from dist_tester import Runner

def test_double_mnist_colparallel():
    """
    测试双卡MNIST 数据并行策略
    """
    expect = {'gpu0': [2.4676132202148438, 0.39483708143234253, 0.23406602442264557, 0.1810654103755951, 0.20704427361488342, 0.47910040616989136, 0.18399205803871155, 0.23776859045028687, 0.28450173139572144, 0.17525523900985718], 'gpu1': [2.5078115463256836, 2.5077714920043945, 2.42617130279541, 2.2883527278900146, 2.452329635620117, 2.398923635482788, 2.4044649600982666, 2.361182928085327, 2.354936122894287, 2.328887939453125]}
    r = Runner(case_file="dist_SimpleNet_2_Cards_ColParallel.py", gpus="0,1", expect=expect)
    r.run()


def test_quadra_mnist_colparallel():
    """
    4 cards
    """
    expect = {'gpu0': [2.2104437351226807, 0.44356533885002136, 0.3702784776687622, 0.2589098811149597, 0.24105454981327057], 'gpu1': [2.5274112224578857, 2.4810233116149902, 2.557343006134033, 2.395901918411255, 2.2790660858154297], 'gpu2': [2.5117580890655518, 2.5019350051879883, 2.2896251678466797, 2.404531478881836, 2.4536967277526855], 'gpu3': [2.4692859649658203, 2.519381284713745, 2.4588584899902344, 2.5196778774261475, 2.365373134613037]}
    r = Runner(case_file="dist_SimpleNet_4_Cards_ColParallel.py", gpus="0,1,2,3", expect=expect)
    r.run()


def test_octa_mnist_colparallel():
    """
    8 cards
    """
    expect = {'gpu0': [2.318121910095215, 0.5388099551200867, 0.4123990833759308], 'gpu1': [2.378802537918091, 2.5928263664245605, 2.4810566902160645], 'gpu2': [2.310807943344116, 2.3566136360168457, 2.4079790115356445], 'gpu3': [2.328518867492676, 2.422605037689209, 2.6101694107055664], 'gpu4': [2.4662084579467773, 2.4323935508728027, 2.576342821121216], 'gpu5': [2.3799145221710205, 2.4984099864959717, 2.4910531044006348], 'gpu6': [2.2620344161987305, 2.5337677001953125, 2.6303534507751465], 'gpu7': [2.343736171722412, 2.33837628364563, 2.3632001876831055]}
    r = Runner(case_file="dist_SimpleNet_8_Cards_ColParallel.py", gpus="0,1,2,3,4,5,6,7", expect=expect)
    r.run()


def test_double_mnist_rowparallel():
    """
    测试双卡MNIST 数据并行策略
    """
    expect = {'gpu0': [2.4631361961364746, 0.5310558676719666, 0.36472272872924805, 0.2792612314224243, 0.30670344829559326, 0.2595176100730896, 0.5333417057991028, 0.2358129322528839, 0.4808518588542938, 0.26858511567115784], 'gpu1': [2.389829158782959, 2.4654831886291504, 2.478320598602295, 2.3023104667663574, 2.4322171211242676, 2.473396062850952, 2.419858455657959, 2.2662954330444336, 2.3250579833984375, 2.305185317993164]}
    r = Runner(case_file="dist_SimpleNet_2_Cards_RowParallel.py", gpus="0,1", expect=expect)
    r.run()


def test_quadra_mnist_rowparallel():
    """
    4 cards
    """
    expect = {'gpu0': [2.467782497406006, 1.1197055578231812, 1.1286476850509644, 0.8998502492904663, 0.9269237518310547], 'gpu1': [2.440591812133789, 2.3763186931610107, 2.4427385330200195, 2.3099918365478516, 2.382205009460449], 'gpu2': [2.333449363708496, 2.328613758087158, 2.3530147075653076, 2.2934279441833496, 2.3364882469177246], 'gpu3': [2.462728500366211, 2.3289785385131836, 2.3672714233398438, 2.459446430206299, 2.3346879482269287]}
    r = Runner(case_file="dist_SimpleNet_4_Cards_RowParallel.py", gpus="0,1,2,3", expect=expect)
    r.run()


def test_octa_mnist_rowparallel():
    """
    8 cards
    """
    expect = {'gpu0': [2.5794143676757812, 1.4855316877365112, 1.6982253789901733], 'gpu1': [2.4848740100860596, 2.344670534133911, 2.311134099960327], 'gpu2': [2.4965426921844482, 2.271151542663574, 2.3089962005615234], 'gpu3': [2.4222099781036377, 2.3143341541290283, 2.310182571411133], 'gpu4': [2.502100706100464, 2.3117117881774902, 2.3244118690490723], 'gpu5': [2.460139274597168, 2.28237247467041, 2.3168325424194336], 'gpu6': [2.3774828910827637, 2.315549373626709, 2.3222386837005615], 'gpu7': [2.305180072784424, 2.337787628173828, 2.303305149078369]}
    r = Runner(case_file="dist_SimpleNet_8_Cards_RowParallel.py", gpus="0,1,2,3,4,5,6,7", expect=expect)
    r.run()