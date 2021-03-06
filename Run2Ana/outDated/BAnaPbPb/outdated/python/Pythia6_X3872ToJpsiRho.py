import FWCore.ParameterSet.Config as cms
from Configuration.Generator.PythiaUESettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            operates_on_particles = cms.vint32(20443,445),
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
#            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Onia_chic_jpsigamma.dec'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Onia_mumu_withX3872.dec'),
#            list_forced_decays = cms.vstring('Mychi_c1','Mychi_c2'),
            list_forced_decays = cms.vstring('myX3872'),

        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0031),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(13775390),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=61          ! Quarkonia',
            'MDME(858,1) = 0  ! 0.060200    e-    e+',
            'MDME(859,1) = 1  ! 0.060100    mu-  mu+',
            'MDME(860,1) = 0  ! 0.879700    rndmflav        rndmflavbar',
            'MSTP(142)=2      ! turns on the PYEVWT Pt re-weighting routine',
            'PARJ(13)=1.000   ! probability that a c or b meson has S=1',
            'PARJ(14)=0.000   ! probability that a meson with S=0 is produced with L=1, J=1',
            'PARJ(15)=0.000   ! probability that a meson with S=1 is produced with L=1, J=0',
            'PARJ(16)=0.660   ! probability that a meson with S=1 is produced with L=1, J=1',
            'PARJ(17)=0.330   ! probability that a meson with S=1 is produced with L=1, J=2',
            'MSTP(145)=0      ! choice of polarization',
            'MSTP(146)=0      ! choice of polarization frame ONLY when mstp(145)=1',
            'MSTP(147)=0      ! particular helicity or density matrix component when mstp(145)=1',
            'MSTP(148)=1      ! possibility to allow for final-state shower evolution, extreme case !',
            'MSTP(149)=1      ! if mstp(148)=1, it determines the kinematics of the QQ~3S1(8)->QQ~3S1(8)+g branching',
            'PARP(141)=1.16   ! New values for COM matrix elements',
            'PARP(142)=0.0119 ! New values for COM matrix elements',
            'PARP(143)=0.01   ! New values for COM matrix elements',
            'PARP(144)=0.01   ! New values for COM matrix elements',
            'PARP(145)=0.05   ! New values for COM matrix elements',
            'PARP(146)=9.28   ! New values for COM matrix elements',
            'PARP(147)=0.15   ! New values for COM matrix elements',
            'PARP(148)=0.02   ! New values for COM matrix elements',
            'PARP(149)=0.02   ! New values for COM matrix elements',
            'PARP(150)=0.085  ! New values for COM matrix elements',
            'BRAT(861)=1.000  ! chi_2c->J/psi gamma',
            'BRAT(862)=0.000  ! chi_2c->rndmflav rndmflavbar',
            'BRAT(1501)=0.013 ! chi_0c->J/psi gamma',
            'BRAT(1502)=0.987 ! chi_0c->rndmflav rndmflavbar',
            'BRAT(1555)=1.000 ! chi_1c->J/psi gamma',
            'BRAT(1556)=0.000 ! chi_1c->rndmflav rndmflavbar'
        ),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters',
            'CSAParameters'),
        CSAParameters = cms.vstring('CSAMODE = 6     ! cross-section reweighted quarkonia')
    )
)

###########
# Filters #
###########
Xfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(20443),
    MaxEta = cms.untracked.double(3.0),
    MinEta = cms.untracked.double(-3.0),
    MinPt = cms.untracked.double(5.0),
	Status = cms.untracked.int32(2),
)

XDaufilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    ParticleID = cms.untracked.int32(20443),
    DaughterIDs = cms.untracked.vint32(443, 113),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

jpsifilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(20443),
    ParticleID = cms.untracked.int32(443),
    DaughterIDs = cms.untracked.vint32(13, -13),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    NumberDaughters = cms.untracked.int32(2),
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(2.0),
    MaxInvMass = cms.untracked.double(4.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

rhofilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(20443),
    ParticleID = cms.untracked.int32(113),
    DaughterIDs = cms.untracked.vint32(211, -211),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

ProductionFilterSequence = cms.Sequence(generator*Xfilter*XDaufilter*jpsifilter*mumugenfilter*rhofilter)
