import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUESettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            use_default_decay = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
#            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bu_JpsiK.dec'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bs_Jpsiphi_mumuKK.dec'),
#            list_forced_decays = cms.vstring('MyB+', 
#                'MyB-'),
            list_forced_decays = cms.vstring('MyB_s0','Myanti-B_s0'),
            operates_on_particles = cms.vint32(0)
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.0003114),#11/30000 445/1600000 
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(2760.0),
    crossSection = cms.untracked.double(54402709.5),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model'),
        bbbarSettings = cms.vstring('MSEL = 1'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'bbbarSettings')
    )
)

jpsifilter = cms.EDFilter("PythiaDauVFilter",
#    MotherID = cms.untracked.int32(521),
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(443),
    DaughterIDs = cms.untracked.vint32(13, -13),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

bfilter = cms.EDFilter("PythiaFilter",
#    MinEta = cms.untracked.double(-9999.0),
    ParticleID = cms.untracked.int32(531),
    MaxEta = cms.untracked.double(3.0),
    MinEta = cms.untracked.double(-3.0),
    MinPt = cms.untracked.double(5.0)
)


kfilter = cms.EDFilter("PythiaDauVFilter",
#    MotherID = cms.untracked.int32(0),
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(333),
    DaughterIDs = cms.untracked.vint32(321, -321),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)


#ProductionFilterSequence = cms.Sequence(generator+bfilter+jpsifilter+kfilter)
#ProductionFilterSequence = cms.Sequence(generator+bfilter+jpsifilter)
#ProductionFilterSequence = cms.Sequence(generator+bfilter+kfilter)
ProductionFilterSequence = cms.Sequence(generator+bfilter)
