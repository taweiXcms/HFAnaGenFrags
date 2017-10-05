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
            operates_on_particles = cms.vint32(),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            user_decay_file = cms.vstring('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec'),
            list_forced_decays = cms.vstring('myD0', 'myanti-D0')
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(     
            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 0.', #min pthat
            'PromptPhoton:all = on',
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(4) # 4 for prompt D0 and 5 for non-prompt D0
	)

D0Daufilter = cms.EDFilter("PythiaMomDauFilter",
    ParticleID = cms.untracked.int32(421),
    MomMinPt = cms.untracked.double(0.),
    MomMinEta = cms.untracked.double(-2.4),
    MomMaxEta = cms.untracked.double(2.4),
    DaughterIDs = cms.untracked.vint32(-321, 211),
    NumberDaughters = cms.untracked.int32(2),
    NumberDescendants = cms.untracked.int32(0),
)

photonFilter = cms.EDFilter("PythiaFilterMultiMother",
	Status = cms.untracked.int32(1),
	MinPt = cms.untracked.double(15.0),
	ParticleID = cms.untracked.int32(22),
	MotherIDs = cms.untracked.vint32(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,-22,-21,-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1)
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*D0Daufilter*photonFilter)
