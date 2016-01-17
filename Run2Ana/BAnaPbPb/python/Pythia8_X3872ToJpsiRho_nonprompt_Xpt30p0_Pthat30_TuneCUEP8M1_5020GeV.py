import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(5020.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/Onia_mumu_withX3872.dec'),
            list_forced_decays = cms.vstring('myX3872'),
            operates_on_particles = cms.vint32()
            ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
#            'HardQCD:all = on',
            'HardQCD:gg2bbbar    = on ',
            'HardQCD:qqbar2bbbar = on ',
            'HardQCD:hardbbbar   = on',
            'PhaseSpace:pTHatMin = 30.',
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

BJpsiDaufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(20443),
    MomMinPt = cms.untracked.double(30.),
    MomMinEta = cms.untracked.double(-2.4),
    MomMaxEta = cms.untracked.double(2.4),
    DaughterIDs = cms.untracked.vint32(443, 113),
    NumberDaughters = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(443),
    DescendantsIDs = cms.untracked.vint32(13, -13),
    NumberDescendants = cms.untracked.int32(2),
    MinEta = cms.untracked.double(-2.5),
    MaxEta = cms.untracked.double(2.5),
)

BX3872Daufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(20443),
    MomMinPt = cms.untracked.double(30.),
    MomMinEta = cms.untracked.double(-2.4),
    MomMaxEta = cms.untracked.double(2.4),
    DaughterIDs = cms.untracked.vint32(443, 113),
    NumberDaughters = cms.untracked.int32(2),
    DaughterID = cms.untracked.int32(113),
    DescendantsIDs = cms.untracked.vint32(211, -211),
    NumberDescendants = cms.untracked.int32(2),
)
bfilter = cms.EDFilter("PythiaFilter",
                       ParticleID = cms.untracked.int32(5)
                       )

ProductionFilterSequence = cms.Sequence(generator*mumugenfilter*BJpsiDaufilter*BX3872Daufilter*bfilter)
