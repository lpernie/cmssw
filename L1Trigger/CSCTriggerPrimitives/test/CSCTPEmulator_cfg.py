# Configuration file to unpack CSC digis, run Trigger Primitives emulator,
# and compare LCTs in the data with LCTs found by the emulator.
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
process = cms.Process("CSCTPEmulator", eras.Run2_2018)

process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10000)
)

# Add "test" directory to the python path.
import sys, os
sys.path.insert(0, os.path.join(os.environ['CMSSW_BASE'], 'src/L1Trigger/CSCTriggerPrimitives/test'))

process.source = cms.Source("PoolSource",
     fileNames = cms.untracked.vstring(
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/4EBDBAC5-D8A6-E811-9D47-FA163E147082.root', 
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/94338DBE-D8A6-E811-97DC-FA163E6B427B.root', 
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/46368DBE-D8A6-E811-BD7C-FA163E6B427B.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/E0E964C1-D8A6-E811-AE4E-FA163EECEDCF.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/A4DC520C-DAA6-E811-844B-FA163E9142A0.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/D26118E0-D8A6-E811-B336-FA163E2EE3A8.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/481944BE-D8A6-E811-9C5B-FA163EC8DFDC.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/AC3523CD-D8A6-E811-887C-FA163EAB6554.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/56001B0F-DAA6-E811-9006-FA163E814B6A.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/5C8F1B6E-DBA6-E811-A8D9-FA163E8DC37A.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/FE7EB818-DAA6-E811-A806-FA163E7121A5.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/8C3A3272-DBA6-E811-BFDA-FA163E5FA5D4.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/2424B212-DAA6-E811-AD48-FA163E6EC3E9.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/CC68247B-DBA6-E811-B987-02163E0176C6.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/209F1C76-DBA6-E811-8ACF-FA163EFD8406.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/AE117A90-DBA6-E811-8F54-02163E01A154.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/FC1F7273-DBA6-E811-A66F-FA163E061B87.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/245FD378-DBA6-E811-8AF5-FA163EEFB5F4.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/A807426F-DBA6-E811-B945-FA163E9F932A.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/8099C388-DBA6-E811-B5D3-FA163E53EEFE.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/B2EC7876-DBA6-E811-AD67-FA163E108BAA.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/18A51D72-DBA6-E811-A60D-FA163EC92B39.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/165E3B70-DBA6-E811-974D-FA163E225AB4.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/C0380874-DBA6-E811-ADA1-FA163E1C00B3.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/2C028F76-DBA6-E811-AC6C-FA163ED07727.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/AC0F4376-DBA6-E811-BABD-02163E01A17C.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/923CAEC4-DCA6-E811-B9DD-FA163ED59DED.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/3015E379-DBA6-E811-ACA9-FA163E6C72EF.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/F078DC7A-DBA6-E811-8C26-FA163E51BE90.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/FE2C32C6-DCA6-E811-AB0B-FA163E1B9BC3.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/70C85DC4-DCA6-E811-8BBC-FA163EB83C02.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/E81ECCC3-DCA6-E811-916C-FA163E5755B1.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/54F2F074-DBA6-E811-9ECF-FA163E2EE3A8.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/1A95A5C4-DCA6-E811-A7F1-FA163EE2EC5A.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/08B5BAC4-DCA6-E811-903E-FA163E9B9A21.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/C266E674-DBA6-E811-974F-FA163EF478A0.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/7A674076-DBA6-E811-994A-02163E01A17C.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/C4633374-DBA6-E811-9C6A-FA163E94348E.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/D4774782-DBA6-E811-AFD6-FA163E170ECE.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/50034073-DBA6-E811-B5C9-FA163E33E510.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/F4373578-DBA6-E811-B0CE-FA163EDAA2B4.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/FE3CCAC8-DCA6-E811-91CF-FA163EBF76CA.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/B0FFD57F-DCA6-E811-8E42-FA163E7AD6B5.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/CCF11D8F-DBA6-E811-9693-02163E010CB1.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/B4AFE288-DBA6-E811-A267-FA163E4642C6.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/18F47FD3-DCA6-E811-93A5-02163E010DF8.root',
         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/321/710/00000/547E9ADA-DBA6-E811-B0A2-FA163E72BD86.root'

#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D423BAA4-BF95-E811-A79C-FA163EDE5CFD.root', 
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D468DACE-A395-E811-91D1-FA163E7E5BB3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D4E2AFC2-A195-E811-B337-FA163E395E49.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D4F0F450-BB95-E811-8BC9-FA163E0AB4C0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D6000C0C-AA95-E811-8CEC-FA163EDF749C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D6730242-AB95-E811-896E-02163E00C478.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D67596AD-B395-E811-A472-FA163E5BDB45.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D68F63E6-AC95-E811-951F-FA163E5B30F8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D6E7BB7B-AD95-E811-BD03-FA163E354E33.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D8E11E7E-A695-E811-9C7E-FA163E2E5B91.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D8E799BF-B695-E811-B968-FA163E60A5FD.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/D8FD2983-B695-E811-A545-FA163E825C6B.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DA1130CB-A795-E811-ADD8-02163E010F05.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DA4B7D1D-B595-E811-A168-FA163E7CAD4F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DA6D6EC4-BE95-E811-9BD8-FA163E41C7B0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DA82EECD-A295-E811-A64F-FA163E138F08.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DC24D32B-BC95-E811-9546-FA163E8A3060.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DC46BE82-AD95-E811-91D6-FA163E4EF997.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DC55CD7D-B295-E811-9448-FA163E102682.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DCBD0C38-BF95-E811-936F-02163E019F19.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DCE626AA-BE95-E811-87FF-FA163ED03425.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DCF45D97-A095-E811-A4A4-FA163EBE4F8C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DE13AB90-B195-E811-926D-FA163E592A6F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DE250E90-A695-E811-A23C-FA163ED2DE85.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DE6254BD-B495-E811-AD81-FA163EE6485C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DE693E17-B595-E811-B725-FA163E548540.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/DEB7947C-A695-E811-B36C-FA163E97A487.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E00CDF65-BC95-E811-BB73-FA163EFA355F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E05464B2-BB95-E811-81DA-FA163E3EE95B.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E0606FC1-B895-E811-ADD5-FA163EF93AEC.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E066F300-B895-E811-A733-FA163E64634F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E0B98B38-B895-E811-B1AA-FA163ED5F2E4.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E22384DF-AC95-E811-9A92-FA163EC64BA5.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2291D46-BB95-E811-9B25-FA163EE6286A.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E267DD6D-A495-E811-A490-FA163ECB3C90.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E26F2CAD-BD95-E811-8E2F-FA163E2DB2A3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2806E90-B995-E811-9F65-FA163E2E65AB.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2816322-B495-E811-A647-FA163E44FC66.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2B723A5-BD95-E811-AB37-FA163E230A11.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2C56865-AF95-E811-A5F4-FA163E20E52E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E2DBD220-B595-E811-85C9-FA163E9D8D04.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E42A422A-AF95-E811-B959-FA163E78BFE5.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E447E1E8-BB95-E811-A672-A4BF0114CB20.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E47BEDFB-B395-E811-B0F7-02163E0164E1.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E4DC1F9E-AB95-E811-A342-FA163E862C57.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E6955780-B395-E811-8CEA-FA163E5874FD.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E6AA4821-B795-E811-AE35-FA163EFE9C39.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E80F7199-BE95-E811-99E5-FA163EABE0AA.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E833DBD1-B195-E811-B17D-FA163EC3CDA2.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/E86F5F8B-AB95-E811-ABEB-02163E00B8BA.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EA5981A5-B095-E811-9E85-FA163E85FA06.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EA88845F-B095-E811-8A38-FA163E862C57.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EA8BFA31-BF95-E811-9B83-FA163E39A19D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EC59BF16-AA95-E811-834D-FA163EEF5766.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EC7B84C3-A295-E811-AB2F-FA163E356356.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EC9E91CA-A295-E811-8659-FA163E741841.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/ECC43DDF-AC95-E811-B4FD-FA163E09BE42.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/ECC62B56-AF95-E811-B358-FA163E777246.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/ECDFEC3B-B895-E811-A1C9-FA163EB7B53C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EE192A0D-A595-E811-AA50-FA163E471DF7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EE3FF1CC-A795-E811-8CB5-FA163E6A17B9.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EE4D28A4-BD95-E811-A037-02163E010DC5.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EE73138A-B295-E811-8C75-02163E016CFB.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EE89FFC9-A795-E811-9F18-FA163E536B65.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EEB9B5F3-B095-E811-B5B9-02163E017755.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/EEFE6043-BC95-E811-8ADE-FA163E99485E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F0109BA8-BD95-E811-9998-FA163E80C212.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F07BD50C-AA95-E811-8158-FA163E0BCDBC.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F09331E1-AC95-E811-9C6D-FA163ED919B8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F09CB028-BA95-E811-8D91-FA163E3CEA02.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F216A4C2-A195-E811-A5CE-FA163E592A6F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F21F748A-A695-E811-A66A-02163E01A01E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F2AF5A7B-AD95-E811-B1FF-FA163EE01A64.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F2F71F67-6D96-E811-AAB7-FA163EC82417.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F42253C7-AD95-E811-A036-FA163EC43B85.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F433BFD7-B695-E811-88C2-FA163EE72A6E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F4B8C3B5-B895-E811-85C9-FA163ECFA4D9.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F619E976-AB95-E811-BE0A-FA163E3CEA02.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F658C678-B095-E811-A0BF-FA163ED03425.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F669CF79-B395-E811-B247-FA163EE8287C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F808DDAC-B395-E811-9772-02163E019EEF.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F837FE02-B895-E811-911D-FA163EAC4CED.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F83C3809-AA95-E811-9F15-FA163ED2DE85.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F8C5C8B8-B395-E811-A02C-FA163E76E4F3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/F8CC34EC-B795-E811-833A-FA163E1E24E8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA2405CD-A795-E811-B975-FA163EB7A855.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA5BB6CC-AB95-E811-BC3B-FA163E302745.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA76D5B3-B795-E811-A902-02163E014DA0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA7E5796-A095-E811-AD7E-FA163E56D1F9.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA9DFDC4-A295-E811-95D8-FA163EAC9FC3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FA9E07C5-A195-E811-8B22-02163E01A01A.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FAD6CD98-B195-E811-8D58-FA163EE655A1.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FAD7515E-A395-E811-AB07-FA163E1ED108.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FAEAF2FD-9F95-E811-A761-FA163E336D90.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FC014FE0-B695-E811-BD41-FA163E77F338.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FC0E37E0-AD95-E811-9F2E-FA163E862C57.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FC2A6453-BF95-E811-95CC-FA163EC417AB.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FCBF028D-B195-E811-A178-FA163E55CE78.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FCDBD7C3-A295-E811-94C0-FA163E354E33.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FCE07AC1-A295-E811-8374-FA163E64F48C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/688/00000/FEF10072-B395-E811-A886-FA163E1A61E2.root'

#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0017C3AA-4195-E811-8858-02163E00BE7D.root', 
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/006BFC46-5E95-E811-A864-FA163EB85ED6.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/02332991-4595-E811-B3B4-FA163EA80540.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/02336CBF-3D95-E811-9CD2-02163E01618A.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0259FACC-3A95-E811-946C-FA163EDB55C0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/025E51B1-4095-E811-9937-02163E010F44.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/046AE05C-4D95-E811-94AA-FA163EF90889.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/04B2E433-6195-E811-9D7E-FA163E74E0ED.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/06106CCF-3395-E811-BFCF-02163E0148F4.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/067672C6-4395-E811-9D24-FA163EC95E7D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/06899B31-3D95-E811-9DBF-FA163E45DF35.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/06B86F84-3C95-E811-98B1-FA163EC95E7D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/06BE2C9C-3E95-E811-932A-02163E019F9E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/06D73618-4A95-E811-AB20-FA163EDF56C7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/087BA342-3595-E811-B816-FA163EEB4452.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/08E65AF8-4895-E811-ADFF-FA163E7D2619.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0A438F64-5895-E811-8700-FA163E057DA4.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0A51D70B-5195-E811-BDAF-FA163EE74B92.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0AC2549E-3995-E811-8624-FA163EC22C2E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/0E3DF5B3-3B95-E811-ADFF-FA163E7DBAC6.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/10858DC2-3B95-E811-BB59-FA163EA1F4CF.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1203A8C6-4795-E811-85CC-A4BF0112F7B8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/125F66BA-5795-E811-8B09-FA163E7ECD23.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/12B6F640-3595-E811-99DF-FA163EEADE18.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/144C2A24-5E95-E811-988D-FA163E2AA51E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/160418B5-4395-E811-B9B6-FA163E9393A6.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1653AF8D-6195-E811-99B5-FA163EE78FEA.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1692F32E-3895-E811-9847-FA163E8467AA.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1843EB0E-5395-E811-B4F4-FA163E22267B.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1A4F82E7-5C95-E811-9BFB-02163E01617E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1C3741B5-3695-E811-9A56-FA163EB4C291.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1C618F6F-4095-E811-A66B-FA163E82F15F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1CCB2448-4F95-E811-8A8C-FA163EE28A99.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1E69C295-5095-E811-8CE4-02163E01A08F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/1E8FFAB1-4995-E811-8E65-FA163EDAABC0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/22F53FD7-3D95-E811-AAAF-FA163ED8122F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2418F46D-5095-E811-B5E3-FA163E71ECF7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/241F4858-4295-E811-9EA9-FA163E0BA45D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/241F90A9-3A95-E811-AA96-FA163EE74B92.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2482FC1C-4395-E811-AD2F-FA163E72781F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/263E783F-5095-E811-A6BC-FA163E7BA7BE.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/26A5C4FE-5595-E811-BDCC-FA163E2322D8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/285CFB82-4195-E811-AD01-02163E013045.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/28672494-5B95-E811-AAB6-FA163EF6014E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2C1A55FF-4495-E811-BEF4-FA163E8ECDD2.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2C2A28DA-3B95-E811-9348-FA163E9071B7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2C8101DE-6195-E811-81BA-FA163E39AE41.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2CF705A9-3A95-E811-9C2C-FA163EF607E3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2EA6AE37-5295-E811-AA69-FA163E7B5F86.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2EC9C92E-4F95-E811-84A6-FA163E5469DB.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/2EFFA12F-4595-E811-83A5-FA163E3A97DC.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/303661B4-3695-E811-93B8-FA163E98D21C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/30450C9D-3995-E811-ADFA-FA163E3C0C41.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3093A1A9-5895-E811-A29C-02163E010C9D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/328F0469-6095-E811-82BF-FA163ED78DED.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/32D7DEFD-4495-E811-AEEA-FA163E0148DD.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/32EF3B2F-3A95-E811-B5AB-FA163EA418F2.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/34CCF1D3-5A95-E811-BB81-FA163E09752E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/36A07842-3595-E811-A8BC-02163E01493D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/36F02F21-3B95-E811-B467-FA163E3B90A3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3807A56A-5995-E811-A5C8-FA163EA5C966.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3887A1B5-5595-E811-81FD-FA163EA5C966.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3A428340-4A95-E811-B6FC-FA163E192E5D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3AD02A99-4895-E811-BB06-02163E01A01E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3C4F6608-3B95-E811-A3EE-02163E01A0F1.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3C999C6E-4095-E811-A8A8-FA163E89857D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3CAA2E33-4295-E811-937A-FA163E047E67.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3CE2190D-5495-E811-992A-FA163E7F5F92.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/3CEA4566-5D95-E811-B834-FA163E3A5F0F.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/406C04A5-3995-E811-8AC7-FA163EFB3A1C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/42BA3171-5995-E811-AA9A-02163E010DFC.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/42C23D84-3C95-E811-A451-FA163E4849C0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/44DF8641-3595-E811-ABC6-FA163E48F6F7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/488DB017-4C95-E811-A645-02163E017F52.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/48C10283-3C95-E811-A47D-FA163EF4C6B1.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/4A1E570E-4E95-E811-B737-FA163E8B095A.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/4A306E13-5C95-E811-A0F6-FA163EE723F8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/4C2310D7-5195-E811-9250-FA163EF250BA.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/4EBCB6B5-3695-E811-B93E-FA163E9A58AD.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5004B8FC-3F95-E811-81EE-FA163E24B9CF.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/50297DDC-5295-E811-AA82-FA163EA266E8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/50791D1B-4795-E811-B3DD-FA163E984001.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5081467F-4895-E811-85E0-FA163EDB426C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/52441545-3595-E811-8A76-02163E01493D.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/524B14B5-5F95-E811-989E-FA163E6C7B05.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/52A3D350-3E95-E811-8DF4-FA163EFBCAE7.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/52C39D3B-4B95-E811-975A-FA163E836BB3.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/549362F0-5995-E811-A704-FA163EE8C9C6.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5631C621-5295-E811-9717-FA163E336D90.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/56990E6D-4795-E811-8D5C-FA163E01971C.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5848AAB0-5795-E811-AA12-FA163EF2167E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5CA2BC5D-3F95-E811-B9F6-A4BF0112BD52.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5E6AF35C-3F95-E811-A2D8-FA163E641B8E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5EA091B3-4695-E811-A6BD-A4BF0112F7B8.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5EBE6212-3A95-E811-85E1-02163E014CBC.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5EEB7F34-5095-E811-BA39-FA163E134929.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/5EFBD7C8-5895-E811-A30F-FA163E4EC205.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/60BFEE85-3C95-E811-958F-FA163E4849C0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/60D0C577-4995-E811-87E2-02163E01650B.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/673/00000/62D560F5-5695-E811-A46E-02163E010C72.root'

#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/500/00000/BC8C0D64-EF93-E811-81A5-02163E00C22E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/569/00000/125EA25B-7C94-E811-B4AB-FA163EBE1F9E.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/570/00000/60340238-8F94-E811-9ED1-FA163ECFE796.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/570/00000/E8CC730A-8F94-E811-9A27-A4BF0114C8F0.root',
#         'file:/eos/cms//store/data/Run2018D/SingleMuon/RAW/v1/000/320/571/00000/A40AD622-9394-E811-9F31-02163E016590.root'
     )
##        untracked uint32 debugVebosity = 10
##        untracked bool   debugFlag     = false
)

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring("debug"),
    debug = cms.untracked.PSet(
        extension = cms.untracked.string(".txt"),
        threshold = cms.untracked.string("DEBUG"),
        lineLength = cms.untracked.int32(132),
        noLineBreaks = cms.untracked.bool(True)
    ),
    # debugModules = cms.untracked.vstring("*")
    debugModules = cms.untracked.vstring("cscTriggerPrimitiveDigis",
        "lctreader")
)

# endcap muon only...
process.load("Geometry.MuonCommonData.muonEndcapIdealGeometryXML_cfi")
# Needed according to Mike Case's e-mail from 27/03.
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
# flags for modelling of CSC geometry
process.load("Geometry.CSCGeometry.cscGeometry_cfi")

process.load("Configuration/StandardSequences/FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '102X_dataRun2_Prompt_v1'

# magnetic field (do I need it?)
# ==============================
process.load('Configuration.StandardSequences.MagneticField_38T_cff')

# CSC raw --> digi unpacker
# =========================
process.load("EventFilter.CSCRawToDigi.cscUnpacker_cfi")
process.muonCSCDigis.InputObjects = "rawDataCollector"
# InputObjects = cms.InputTag("cscpacker","CSCRawData")
# for run 566 and 2008 data
# ErrorMask = cms.untracked.uint32(0xDFCFEFFF)

# CSC Trigger Primitives configuration
# ====================================
#process.load("L1TriggerConfig.L1CSCTPConfigProducers.L1CSCTriggerPrimitivesConfig_cff")
#process.load("L1TriggerConfig.L1CSCTPConfigProducers.L1CSCTriggerPrimitivesDBConfig_cff")
#process.prefer("l1csctpdbconfsrc")
#process.l1csctpconf.alctParamMTCC2.alctNplanesHitPretrig = 3
#process.l1csctpconf.alctParamMTCC2.alctNplanesHitAccelPretrig = 3
#process.l1csctpconf.clctParam.clctNplanesHitPretrig = 3
#process.l1csctpconf.clctParam.clctHitPersist = 4
#process.l1csctpconf.alctParamMTCC2.alctDriftDelay = 9
#process.l1csctpconf.alctParamMTCC2.alctL1aWindowWidth = 9

# CSC Trigger Primitives emulator
# ===============================
process.load("L1Trigger.CSCTriggerPrimitives.cscTriggerPrimitiveDigis_cfi")
process.cscTriggerPrimitiveDigis.alctParam07.verbosity = 2
process.cscTriggerPrimitiveDigis.clctParam07.verbosity = 2
process.cscTriggerPrimitiveDigis.tmbParam.verbosity = 2
process.cscTriggerPrimitiveDigis.CSCComparatorDigiProducer = "muonCSCDigis:MuonCSCComparatorDigi"
process.cscTriggerPrimitiveDigis.CSCWireDigiProducer = "muonCSCDigis:MuonCSCWireDigi"
process.cscTriggerPrimitiveDigis.commonParam.isSLHC = cms.bool(False)
process.cscTriggerPrimitiveDigis.commonParam.smartME1aME1b = cms.bool(True)

# CSC Trigger Primitives reader
# =============================
process.load("CSCTriggerPrimitivesReader_cfi")
process.lctreader.debug = True

# Auxiliary services
# ==================
#process.myfilter = cms.EDFilter(
#  'EventNumberFilter',
#  runEventNumbers = cms.vuint32(1,4309, 1,4310)
#)

# Output
# ======
process.output = cms.OutputModule("PoolOutputModule",
    #fileName = cms.untracked.string("/data0/slava/test/lcts_run122909.root"),
    fileName = cms.untracked.string("lcts_run_test.root"),
    outputCommands = cms.untracked.vstring("keep *",
        "drop *_DaqSource_*_*")
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('TPEHists.root')
)

# Scheduler path
# ==============
#process.p = cms.Path(process.myfilter*process.muonCSCDigis*process.cscTriggerPrimitiveDigis*process.lctreader)
process.p = cms.Path(process.muonCSCDigis*process.cscTriggerPrimitiveDigis*process.lctreader)
#process.p = cms.Path(process.muonCSCDigis*process.cscTriggerPrimitiveDigis)
process.ep = cms.EndPath(process.output)
