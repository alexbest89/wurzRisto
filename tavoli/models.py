from django.db import models
from django.urls import reverse


class Tavoli(models.Model):
    """Modello per rappresentare i tavoli"""

    nome_Tavolo = models.CharField(max_length=200, help_text='Inserisci il tavolo (es. Tavolo1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_Tavolo

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('specifica_tavolo', args=[str(self.id)])


class Fornitore(models.Model):
    """Modello per rappresentare i Fornitori"""

    ragione_sociale = models.CharField(max_length=200, help_text="Inserisci la ragione sociale")
    p_Iva = models.CharField(max_length=11, help_text="Inserisci la partita Iva")
    citta = models.CharField(max_length=100, help_text="Inserisci la citta")
    via = models.CharField(max_length=300, help_text="Inserisci la via")
    cap = models.CharField(max_length=5, help_text="Inserisci il CAP")

    def __str__(self):
        return self.ragione_sociale

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Cameriere(models.Model):
    """Modello per rappresentare i Camerieri"""

    nome = models.CharField(max_length=200, help_text="Inserisci il nome")
    cognome = models.CharField(max_length=200, help_text="Inserisci il cognome")
    telefono = models.CharField(max_length=10, help_text="Inserisci il numero di telefono")
    email = models.EmailField(max_length=200, help_text="Inserisci l'indirizzo email")

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Categoria(models.Model):
    nome = models.CharField(max_length=200, default="nome")

    def __str__(self):
        return self.nome


class Prodotti(models.Model):
    """Modello per rappresentare i prodotti"""
    scIva = (
        ('4', '4 %'),
        ('10', '10 %'),
        ('21', '21 %'),
        ('22', '22 %'),
    )
    unMisura = (
        ('pz', 'Pezzi'),
        ('ps', 'Peso'),
        ('lt', 'Litro'),
    )

    descrizione_breve = models.CharField(max_length=20, help_text="Inserisci una descrizione breve MAX 20 caratteri")
    descrizione_lunga = models.CharField(max_length=200, help_text="Inserisci una descrizione")
    unita_di_misura = models.CharField(
        max_length=2,
        choices=unMisura,
        blank=True,
        help_text="Seleziona l'unità di misura"
    )
    # categoria = models.On('Categoria', on_delete=models.CASCADE, default=models.SET_NULL)
    iva = models.CharField(
        max_length=2,
        choices=scIva,
        blank=True,
        help_text="Scegli l'IVA"
    )
    ean = models.CharField(max_length=100, help_text="Inserisci il barcode")
    prezzo_acquisto = models.DecimalField(max_digits=5, decimal_places=2)  # 99999,99
    prezzo_vendita = models.DecimalField(max_digits=5, decimal_places=2)

    id_fornitore = models.ManyToManyField(Fornitore, help_text="Seleziona il fornitore")

    class Meta:
        ordering = ['descrizione_breve']

    def __str__(self):
        return self.descrizione_lunga

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Spec_Tav(models.Model):
    tavolo = models.ForeignKey('Tavoli', on_delete=models.CASCADE)
    prodotto = models.ForeignKey('Prodotti', on_delete=models.CASCADE)
    cameriere = models.ForeignKey('Cameriere', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Scontrino(models.Model):
    num_azz = models.IntegerField()
    num_scon = models.IntegerField()
    tipo_pag = models.CharField(max_length=20, default="pagamento")
    tot = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField( auto_now_add = True)

    def __str__(self):
        return self.num_scon

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Spec_Scon(models.Model):
    id_scon = models.ForeignKey('Scontrino', on_delete=models.CASCADE)
    id_prodotto = models.ForeignKey('Prodotti', on_delete=models.CASCADE)

    def __str__(self):
        return self.id_scon

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])


class Azzeramenti(models.Model):
    num_azz = models.IntegerField(unique=True)
    tot_giornaliero = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
