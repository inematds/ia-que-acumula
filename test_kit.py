import tempfile
import unittest
from pathlib import Path
import jarvis

class Kit(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
  self.base=Path(self.temp.name); self.root=self.base/'jarvis'; jarvis.create(self.root)
 def test_preserva_sistema_existente(self):
  (self.root/'MEMORIA.md').write_text('decisão importante')
  with self.assertRaises(ValueError): jarvis.create(self.root)
  self.assertEqual((self.root/'MEMORIA.md').read_text(),'decisão importante')
 def test_pacote_leva_regras_e_tarefa(self):
  text=jarvis.package(self.root)
  self.assertIn('Não inventar',text); self.assertIn('Bruno',text)
 def test_repo_e_catalogado_sem_executar(self):
  repo=self.base/'repo';repo.mkdir(); (repo/'README.md').write_text('Exemplo');(repo/'executar.sh').write_text('touch PROIBIDO')
  jarvis.incorporate(self.root,repo,'exemplo','fila')
  self.assertFalse((repo/'PROIBIDO').exists())
  import json
  r=json.loads((self.root/'incorporacoes/exemplo.json').read_text())
  self.assertEqual(r['estado'],'aguarda_revisao'); self.assertEqual(len(r['documentos']['README.md']['sha256']),64)
 def test_impede_travessia_e_duplicacao(self):
  repo=self.base/'repo'; repo.mkdir(); (repo/'README.md').write_text('x')
  with self.assertRaises(ValueError): jarvis.incorporate(self.root,repo,'../fora','x')
  jarvis.incorporate(self.root,repo,'exemplo','x')
  with self.assertRaises(ValueError): jarvis.incorporate(self.root,repo,'exemplo','x')
 def test_prova_aceita_exemplo_e_recusa_prazo_inventado(self):
  result=self.root/'resultado.md';result.write_text('Ana | revisar proposta | sexta\nBruno | confirmar reunião | pendente\n')
  self.assertTrue(jarvis.prove(self.root,result)['passou'])
  result.write_text('Ana | sexta\nBruno | segunda\n')
  self.assertFalse(jarvis.prove(self.root,result)['passou'])
 def test_sem_readme_reprova(self):
  repo=self.base/'repo';repo.mkdir()
  with self.assertRaises(ValueError): jarvis.incorporate(self.root,repo,'vazio','x')
 def test_symlink_readme_nao_lido(self):
  repo=self.base/'repo';repo.mkdir();secret=self.base/'segredo';secret.write_text('nunca copiar');(repo/'README.md').symlink_to(secret)
  with self.assertRaises(ValueError): jarvis.incorporate(self.root,repo,'link','x')
if __name__=='__main__': unittest.main()
