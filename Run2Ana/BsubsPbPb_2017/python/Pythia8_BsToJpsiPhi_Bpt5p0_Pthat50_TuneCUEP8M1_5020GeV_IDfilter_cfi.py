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
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Bs_JpsiPhi_V3.dec'),
            list_forced_decays = cms.vstring('MyB_s0','Myanti-B_s0'),
            operates_on_particles = cms.vint32()
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(            
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 50.',
          
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
BJpsiDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(531),
    MomMinPt = cms.untracked.double(5.),
    MomMinEta = cms.untracked.double(-2.8),
    MomMaxEta = cms.untracked.double(2.8),
    DaughterIDs = cms.untracked.vint32(443, 333),
    NumberDaughters = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(443),
    DescendantsIDs = cms.untracked.vint32(13, -13),
    NumberDescendants = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-10000.0),
    MaxEta = cms.untracked.double(10000.0),
)

BPhiDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(531),
    MomMinPt = cms.untracked.double(5.),
    MomMinEta = cms.untracked.double(-2.8),
    MomMaxEta = cms.untracked.double(2.8),
    DaughterIDs = cms.untracked.vint32(443, 333),
    NumberDaughters = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(333),
    DescendantsIDs = cms.untracked.vint32(321, -321),
    NumberDescendants = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-10000.0),
    MaxEta = cms.untracked.double(10000.0),
)

ProductionFilterSequence = cms.Sequence(generator*BJpsiDaufilter*BPhiDaufilter)
