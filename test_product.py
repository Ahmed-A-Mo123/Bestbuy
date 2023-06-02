import pytest
import products


def test_normal_product():
    """Test that creating a normal product works."""
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.is_active() is True


def test_invalid_details():
    """Test that creating a product with invalid details (empty name, negative price) invokes an exception."""
    bose = products.Product("", price=-250, quantity=500, active=True)
    with pytest.raises(ValueError):
        bose.buy(10)


def test_inactive_product():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500, active=True)
    bose.buy(500)
    assert bose.is_active() is False


def test_purchase_modifies_quantity():
    """Test that product purchase modifies the quantity and returns the right output."""
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500, active=True)
    bose.buy(1)
    assert bose.get_quantity() == 499


def test_purchase_more_than_in_stock():
    """Test that buying a larger quantity than exists invokes exception."""
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500, active=True)
    with pytest.raises(ValueError):
        bose.buy(501)



