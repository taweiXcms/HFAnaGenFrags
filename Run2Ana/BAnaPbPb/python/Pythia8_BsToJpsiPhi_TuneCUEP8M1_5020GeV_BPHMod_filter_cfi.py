import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         comEnergy = cms.double(5020.0),
                         crossSection = cms.untracked.double(54000000000),
                         filterEfficiency = cms.untracked.double(3.0e-4),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bs_JpsiPhi_V3.dec'),#only available in 7_1_19
            #user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bs_Jpsiphi_mumuKK.dec'),
            list_forced_decays = cms.vstring('MyB_s0','Myanti-B_s0'),
            operates_on_particles = cms.vint32()
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(            
#           'SoftQCD:nonDiffractive = on',
#           'SoftQCD:singleDiffractive = on',
#           'SoftQCD:doubleDiffractive = on',
            'HardQCD:gg2bbbar    = on ',
            'HardQCD:qqbar2bbbar = on ',
            'HardQCD:hardbbbar   = on',
            'PhaseSpace:pTHatMin = 2.',
          
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########
bfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(531),
    MaxEta = cms.untracked.double(3.0),
    MinEta = cms.untracked.double(-3.0),
    MinPt = cms.untracked.double(5.0)
)

bDaufilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(0),
    ParticleID = cms.untracked.int32(531),
    DaughterIDs = cms.untracked.vint32(443, 333),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

jpsifilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(531),
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

kfilter = cms.EDFilter("PythiaDauVFilter",
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(333),
    DaughterIDs = cms.untracked.vint32(321, -321),
    verbose = cms.untracked.int32(0),
    MinPt = cms.untracked.vdouble(0.0, 0.0),
    MaxEta = cms.untracked.vdouble(9999, 9999),
    MinEta = cms.untracked.vdouble(-9999, -9999),
    NumberDaughters = cms.untracked.int32(2),
)

ProductionFilterSequence = cms.Sequence(generator*bfilter*bDaufilter*jpsifilter*mumugenfilter*kfilter)
