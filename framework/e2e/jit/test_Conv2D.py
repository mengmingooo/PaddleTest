#!/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test jit cases
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "utils"))

from utils.yaml_loader import YamlLoader
from jittrans import JitTrans

yaml_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "yaml", "nn.yml")
yml = YamlLoader(yaml_path)


def test_conv2d_base():
    """test conv2d_base"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_base"))
    jit_case.jit_run()


def test_conv2d_0():
    """test conv2d_0"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_0"))
    jit_case.jit_run()


def test_conv2d_1():
    """test conv2d_1"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_1"))
    jit_case.jit_run()


def test_conv2d_2():
    """test conv2d_2"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_2"))
    jit_case.jit_run()


def test_conv2d_3():
    """test conv2d_3"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_3"))
    jit_case.jit_run()


def test_conv2d_4():
    """test conv2d_4"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_4"))
    jit_case.jit_run()


def test_conv2d_5():
    """test conv2d_5"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_5"))
    jit_case.jit_run()


def test_conv2d_6():
    """test conv2d_6"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_6"))
    jit_case.jit_run()


def test_conv2d_7():
    """test conv2d_7"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_7"))
    jit_case.jit_run()


def test_conv2d_11():
    """test conv2d_11"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_11"))
    jit_case.jit_run()


def test_conv2d_12():
    """test conv2d_12"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_12"))
    jit_case.jit_run()


def test_conv2d_13():
    """test conv2d_13"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_13"))
    jit_case.jit_run()


def test_conv2d_14():
    """test conv2d_14"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_14"))
    jit_case.jit_run()


def test_conv2d_15():
    """test conv2d_15"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_15"))
    jit_case.jit_run()


def test_conv2d_transpose_base():
    """test conv2d_transpose_base"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_base"))
    jit_case.jit_run()


def test_conv2d_transpose_0():
    """test conv2d_transpose_0"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_0"))
    jit_case.jit_run()


def test_conv2d_transpose_1():
    """test conv2d_transpose_1"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_1"))
    jit_case.jit_run()


def test_conv2d_transpose_2():
    """test conv2d_transpose_2"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_2"))
    jit_case.jit_run()


def test_conv2d_transpose_3():
    """test conv2d_transpose_3"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_3"))
    jit_case.jit_run()


def test_conv2d_transpose_4():
    """test conv2d_transpose_4"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_4"))
    jit_case.jit_run()


def test_conv2d_transpose_5():
    """test conv2d_transpose_5"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_5"))
    jit_case.jit_run()


def test_conv2d_transpose_6():
    """test conv2d_transpose_6"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_6"))
    jit_case.jit_run()


def test_conv2d_transpose_7():
    """test conv2d_transpose_7"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_7"))
    jit_case.jit_run()


def test_conv2d_transpose_8():
    """test conv2d_transpose_8"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_8"))
    jit_case.jit_run()


def test_conv2d_transpose_9():
    """test conv2d_transpose_9"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_9"))
    jit_case.jit_run()


def test_conv2d_transpose_10():
    """test conv2d_transpose_10"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_10"))
    jit_case.jit_run()


def test_conv2d_transpose_11():
    """test conv2d_transpose_11"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_11"))
    jit_case.jit_run()


def test_conv2d_transpose_12():
    """test conv2d_transpose_12"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_12"))
    jit_case.jit_run()


def test_conv2d_transpose_13():
    """test conv2d_transpose_13"""
    jit_case = JitTrans(case=yml.get_case_info("conv2d_transpose_13"))
    jit_case.jit_run()