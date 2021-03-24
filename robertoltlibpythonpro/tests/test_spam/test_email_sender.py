import pytest

from robertoltlibpythonpro.spam.email_sender import Sender, InvalidEmail


def test_criate_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'shipper',
    ['rl.beto.lorenzoni@gmail.com', 'foo@bar.com.br']
)
def test_shipper(shipper):
    sender = Sender()

    result = sender.send(shipper,
                         'janine.slorenzoni@gmail.com',
                         'Curso Python Pro',
                         'Inicio das turmas Von Rossom'
                         )
    assert shipper in result


@pytest.mark.parametrize(
    'shipper',
    ['', 'foo']
)
def test_invalid_shipper(shipper):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            shipper,
            'janine.slorenzoni@gmail.com',
            'Curso Python Pro',
            'Inicio das turmas Von Rossom'
        )
