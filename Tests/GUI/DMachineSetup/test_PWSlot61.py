# -*- coding: utf-8 -*-

import sys
from unittest import TestCase

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot61.PWSlot61 import PWSlot61


class test_PWSlot61(TestCase):
    """Test that the widget PWSlot61 behave like it should"""

    def setUp(self):
        """Run at the begining of every test to setup the gui"""

        self.test_obj = LamSlotWind(Rint=0.1, Rext=0.2)
        self.test_obj.slot = SlotW61(
            H0=0.10,
            H1=0.11,
            H2=0.12,
            W0=0.13,
            W1=0.14,
            W2=0.15,
            H3=0.16,
            H4=0.17,
            W3=0.18,
        )
        self.widget = PWSlot61(self.test_obj)

    @classmethod
    def setUpClass(cls):
        """Start the app for the test"""
        print("\nStart Test PWSlot61")
        cls.app = QtWidgets.QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def test_init(self):
        """Check that the Widget spinbox initialise to the lamination value"""

        self.assertEqual(self.widget.lf_H0.value(), 0.10)
        self.assertEqual(self.widget.lf_H1.value(), 0.11)
        self.assertEqual(self.widget.lf_H2.value(), 0.12)
        self.assertEqual(self.widget.lf_W0.value(), 0.13)
        self.assertEqual(self.widget.lf_W1.value(), 0.14)
        self.assertEqual(self.widget.lf_W2.value(), 0.15)
        self.assertEqual(self.widget.lf_H3.value(), 0.16)
        self.assertEqual(self.widget.lf_H4.value(), 0.17)
        self.assertEqual(self.widget.lf_W3.value(), 0.18)

    def test_out(self):
        """Checking output 
        """
        self.test_obj = LamSlotWind(
            Rint=0, Rext=0.1325, is_internal=True, is_stator=False, L1=0.9
        )
        self.test_obj.slot = SlotW61(
            Zs=12,
            W0=15e-3,
            W1=35e-3,
            W2=12.5e-3,
            H0=15e-3,
            H1=20e-3,
            H2=25e-3,
            H3=1e-3,
            H4=2e-3,
            W3=3e-3,
        )
        self.widget = PWSlot61(self.test_obj)
        self.assertEqual(self.widget.out_slot_height.text(), "Slot height: 0.05994 m")
        self.assertTrue(self.widget.out_tooth_width.isHidden())

    def test_set_W0(self):
        """Check that the Widget allow to update W0"""
        self.widget.lf_W0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_W0, "0.31")
        self.widget.lf_W0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W0, 0.31)
        self.assertEqual(self.test_obj.slot.W0, 0.31)

    def test_set_W1(self):
        """Check that the Widget allow to update W1"""
        self.widget.lf_W1.clear()
        QTest.keyClicks(self.widget.lf_W1, str(0.32))
        self.widget.lf_W1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W1, 0.32)
        self.assertEqual(self.test_obj.slot.W1, 0.32)

    def test_set_W2(self):
        """Check that the Widget allow to update W2"""
        self.widget.lf_W2.clear()
        QTest.keyClicks(self.widget.lf_W2, "0.33")
        self.widget.lf_W2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W2, 0.33)
        self.assertEqual(self.test_obj.slot.W2, 0.33)

    def test_set_H0(self):
        """Check that the Widget allow to update H0"""
        self.widget.lf_H0.clear()
        QTest.keyClicks(self.widget.lf_H0, "0.34")
        self.widget.lf_H0.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H0, 0.34)
        self.assertEqual(self.test_obj.slot.H0, 0.34)

    def test_set_H1(self):
        """Check that the Widget allow to update H1"""
        self.widget.lf_H1.clear()
        QTest.keyClicks(self.widget.lf_H1, "0.35")
        self.widget.lf_H1.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H1, 0.35)
        self.assertEqual(self.test_obj.slot.H1, 0.35)

    def test_set_H2(self):
        """Check that the Widget allow to update H2"""
        self.widget.lf_H2.clear()
        QTest.keyClicks(self.widget.lf_H2, "0.36")
        self.widget.lf_H2.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H2, 0.36)
        self.assertEqual(self.test_obj.slot.H2, 0.36)

    def test_set_W3(self):
        """Check that the Widget allow to update W3"""
        self.widget.lf_W3.clear()
        QTest.keyClicks(self.widget.lf_W3, "0.37")
        self.widget.lf_W3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.W3, 0.37)
        self.assertEqual(self.test_obj.slot.W3, 0.37)

    def test_set_H3(self):
        """Check that the Widget allow to update H3"""
        self.widget.lf_H3.clear()
        QTest.keyClicks(self.widget.lf_H3, "0.38")
        self.widget.lf_H3.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H3, 0.38)
        self.assertEqual(self.test_obj.slot.H3, 0.38)

    def test_set_H4(self):
        """Check that the Widget allow to update H4"""
        self.widget.lf_H4.clear()
        QTest.keyClicks(self.widget.lf_H4, "0.39")
        self.widget.lf_H4.editingFinished.emit()  # To trigger the slot

        self.assertEqual(self.widget.slot.H4, 0.39)
        self.assertEqual(self.test_obj.slot.H4, 0.39)
